from maya import cmds
from maya import mel
import shutil
import os

from prins.core.utils   import PathFinder
from prins              import __PROJECTPATH__


def save(workspacePath, type):
    """This function must be called in Maya.
    Saves a new file in the requested location.

    :param workspacePath: The maya workspace folder to save files to
    :type workspacePath: str
    :param type: The type of saving, can be "Asset" or "Shot", defaults to "Asset"
    :type type: str, optional
    :raises TypeError: Raises an error if arg type are wrong
    :raises ValueError: Raises an error if the type arg is not 'Asset' or 'Shot'
    """

    # Sanity check
    if not isinstance(workspacePath, str):
        raise TypeError("workspacePath arg must be of type string")
    if not type in ["Asset", "Shot"]:
        raise ValueError("type arg must be 'Asset' or 'Shot'")

    # Setup PathFinder
    finder = PathFinder(__PROJECTPATH__)
    finder.setTemplateType(type)
    finder.setTemplateName("workspace")
    finder.update_datasFromPath(workspacePath)
    finder.setTemplateType("Files")
    finder.setTemplateFile("maya%s"%type).setTemplateName(finder.templateFile)

    workspaceFilepath = os.path.join(workspacePath, "workspace.mel")
    
    # Create workspace if not existing
    if not os.path.isfile(workspaceFilepath):

        folderpath, filename = os.path.split(os.path.normpath(__file__))
        defaultWorkspaceFilepath = os.path.join(folderpath, "prinsWorkspace.mel")

        try:
            os.makedirs(workspacePath)
        except:
            pass

        shutil.copyfile(defaultWorkspaceFilepath, workspaceFilepath)

    # Get scenes absolute path
    cmds.workspace(workspaceFilepath, o = True)
    root = cmds.workspace(query = True, rd = True)
    scenes = cmds.workspace(fre = "scene")
    scenesPath = os.path.join(root, scenes)

    allScenes = os.listdir(scenesPath)

    # Get version
    if allScenes:
        lastScene = allScenes[-1]
        finder.update_datasFromFilename(lastScene)
    
        while finder.getResult() in allScenes:
            finder.increment_version()

    else:
        finder.update_version(1)

    # Save
    cmds.file(rename = os.path.join(scenesPath, finder.getResult()))
    cmds.file(save = True)

    # Message for the user
    mel.eval('print "> PRINS Successfully saved your file.\\n"')


def publish(publishFilepath, template, override):
    """Publishes selection from Maya.

    :param publishFilepath: The filepath to publish
    :type publishFilepath: str
    :param template: The file template that defines export format.
    :type template: str
    :param override: If true, will force overrides existing files.
    :type override: bool
    :raises TypeError: Raises an error if arg are of the wrong type
    :raises ValueError: Raises an error if args are of the wrong value
    :raises Exception: Raises an error if the scene is not saved
    :raises FileExistsError: If override is false, raises an error to prevent file override.
    """

    # Sanity check
    validTemplates = [
        "mayaAsset",
        "mayaShot",
        "assetAlembic",
        "assetFbx",
        "animFbx",
        "animAlembic"
    ]

    if not isinstance(publishFilepath, str):
        raise TypeError("publishPath arg must be of type string")
    if not template in validTemplates:
        raise ValueError("Unrecognized file template name")
    if cmds.file(query = True, anyModified = True):
        mel.eval('print "> PRINS ERROR, save your scene first.\\n"')
        raise Exception("Scene is not saved.")

    # Abort publish if the filename is not available
    if not override and os.path.isfile(publishFilepath):
        raise FileExistsError("The publish file already exists.")

    # Process the scene
    selection = cmds.ls(sl = True)
    start = cmds.playbackOptions(query = True, animationStartTime = True)
    end = cmds.playbackOptions(query = True, animationEndTime = True)

    publishCommands = {
        "mayaAsset" : lambda absPath, *args : cmds.file(absPath, exportSelected = True, type = "mayaAscii"),
        "assetAlembic" : lambda absPath, *args: cmds.AbcExport(j = "-f %s -sl -u GuerillaTags -uv -ws -wuvs"%absPath),
        "assetFbx" : lambda absPath, *args: mel.eval('FBXExport -f "%s" -s'%(absPath.replace("\\", "/"))),
        "animFbx" : lambda absPath, *args: mel.eval('FBXExport -f "%s" -s'%(absPath.replace("\\", "/"))),
        "animAlembic" : lambda absPath, start, end: cmds.AbcExport(j = "-f %s -sl -u GuerillaTags -uv -ws -wuvs -fr %s %s"%(absPath, start, end))
    }
        
    # Exception for alembic exports
    if "Alembic" in template:
        for sel in selection:
            for child in cmds.listRelatives(sel, allDescendents = True, f = True):
                cmds.select(child, add = True)

    # Publish
    publishCommands[template](publishFilepath, start, end)

    # Reset selection
    cmds.select(clear = True)
    for sel in selection:
        cmds.select(sel, add = True)

    # Message for the user
    mel.eval('print "> PRINS Successfully published your file.\\n"')


def deliver(deliveryFilepath, template, size):
    """Delivers a scene in a video format.

    :param deliveryFilepath: The path to deliver
    :type deliveryFilepath: str
    :param template: The file template that defines export format.
    :type template: str
    :param size: The image size
    :type size: list(int, int)
    :raises ValueError: Raises an error if args are not valid
    :raises TypeError: Raises an error if args are not valid
    :raises Exception: Raises an error if the scene is not up to date
    """

    validTemplates = [
        "movAsset",
        "mp4Asset",
        "movShot",
        "mp4Shot"
    ]

    # Sanity Check
    if not isinstance(deliveryFilepath, str):
        raise TypeError("deliveryPath arg must be of type string")
    if not template in validTemplates:
        raise ValueError("Unrecognized file format")
    if not isinstance(size, list) or not len(size) == 2 or not isinstance(size[0], int):
        raise TypeError("size arg is not valid")
    if cmds.file(query = True, anyModified = True):
        mel.eval('print "> PRINS ERROR, save your scene first.\\n"')
        raise Exception("Scene is not saved.")

    deliverCommands = {
        "movAsset" : lambda filepath, size : cmds.playblast(
            filename = filepath,
            format = "qt",
            wh = size,
            showOrnaments = False,
            quality = 50,
            p = 100,
            fo = True
        ),
        "movShot" : lambda filepath, size : cmds.playblast(
            filename = filepath,
            format = "qt",
            wh = size,
            showOrnaments = False,
            quality = 50,
            p = 100,
            fo = True
        ),
        "mp4Asset" : lambda filepath, size: NotImplementedError("This functionnality is not implemented yet."), #TODO
        "mp4Shot" : lambda filepath, size: NotImplementedError("This functionnality is not implemented yet.") #TODO
    }

    # TODO : supports sound node
    # soundNodes = cmds.ls(type = 'audio')

    # Deliver
    deliverCommands[template](deliveryFilepath, size)

    # Message for the user
    mel.eval('print "> PRINS Successfully delivered your file.\\n"')