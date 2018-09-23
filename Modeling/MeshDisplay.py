import maya.cmds as cmds
import maya.mel as mel


# class name must be 'Commands'
class Commands(object):

    commandDict = {}

    ###########
    # Normals #
    ###########

    def _averagePolygonNormals(self):
        cmds.AveragePolygonNormals()
    commandDict['averagePolygonNormals'] = 'polyNormalAverage.png'

    def _averagePolygonNormalsOptions(self):
        cmds.AveragePolygonNormalsOptions()
    commandDict['averagePolygonNormalsOptions'] = 'polyNormalAverage.png'

    def _conformPolygonNormals(self):
        cmds.ConformPolygonNormals()
    commandDict['conformPolygonNormals'] = 'polyNormalsConform.png'

    def _reversePolygonNormals(self):
        cmds.ReversePolygonNormals()
    commandDict['_reversePolygonNormals'] = 'polyNormal.png'

    def _reversePolygonNormalsOptions(self):
        cmds.ReversePolygonNormalsOptions()
    commandDict['_reversePolygonNormalsOptions'] = 'polyNormal.png'

    def _setNormalAngle(self):
        cmds.SetNormalAngle()
    commandDict['setNormalAngle'] = "polyNormalSetAngle.png"

    def _setToFaceNormals(self):
        cmds.SetToFaceNormals()
    commandDict['setToFaceNormals'] = "polyNormalSetToFace.png"

    def _setToFaceNormalsOptions(self):
        cmds.SetToFaceNormalsOptions()
    commandDict['setToFaceNormalsOptions'] = "polyNormalSetToFace.png"

    def _setVertexNormal(self):
        cmds.SetVertexNormal()
    commandDict['setVertexNormal'] = "polySetVertexNormal.png"

    def _setVertexNormalOptions(self):
        cmds.SetVertexNormalOptions()
    commandDict['setVertexNormalOptions'] = "polySetVertexNormal.png"

    def _hardenEdges(self):
        mel.eval("SoftPolyEdgeElements 0")
    commandDict['hardenEdges'] = "polyHardEdge.png"

    def _softenEdges(self):
        mel.eval("SoftPolyEdgeElements 1")
    commandDict['softenEdges'] = "polySoftEdge.png"

    def _lockNormals(self):
        cmds.LockNormals()
    commandDict['lockNormals'] = "polyNormalLock.png"

    def _unlockNormals(self):
        cmds.UnlockNormals()
    commandDict['unlockNormals'] = "polyNormalUnlock.png"
