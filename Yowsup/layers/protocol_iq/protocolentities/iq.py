from Yowsup.structs import ProtocolEntity, ProtocolTreeNode
class IqProtocolEntity(ProtocolEntity):

    '''
    <iq type="{{get | set?}}" id="{{id}}" xmlns="{{xmlns}}, to={{TO}}">
    </iq>
    '''

    def __init__(self, xmlns, _id = None, _type = None, to = None):
        super(IqProtocolEntity, self).__init__("iq")

        assert _type in ("set", "get"), "Iq of type %s is not implemented, can accept only (set | get)" % _type

        self._id = self._generateId() if _id is None else _id
        self._type = _type
        self.xmlns = xmlns
        self.to = to

    def getId(self):
        return self._id
    
    def toProtocolTreeNode(self):
        attribs = {
            "id"          : self._id,
            "xmlns"       : self.xmlns,
            "type"        : self._type
        }

        if self.to:
            attribs["to"] = self.to

        return self._createProtocolTreeNode(attribs, None, data = None)

    def __str__(self):
        out  = "Iq:\n"
        out += "ID: %s\n" % self._id
        out += "Type: %s\n" % self._type
        out += "xmlns: %s\n" % self.xmlns
        if self.to:
            out += "to: %s\n" % self.to
        return out

    @staticmethod
    def fromProtocolTreeNode(node):
        return IqProtocolEntity(
            node.getAttributeValue("xmlns"),
            node.getAttributeValue("id"),
            node.getAttributeValue("type"),
            node.getAttributeValue("to")
            )
