
class TopicData:
    def __init__(self, topic, fields, data = None):
        self.Topic = topic
        self.Fields = fields
        self.SelectedField = 0
        self.Data = data
        self.LastUpdated = 0