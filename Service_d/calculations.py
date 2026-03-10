from base64 import b64decode


class Calculations:
    def __init__(self,logger):
        self.logger = logger
        self.list_hostile = b64decode("R2Vub2NpZGUsV2FyIENyaW1lcyxBcGFydGhlaWQsTWFzc2FjcmUsTmFrYmEsRGlzcGxhY2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMsQmxvY2thZGUsT2NjdXBhdGlvbixSZWZ1Z2VlcyxJQ0MsQkRT").decode().split(',')
        self.less_hostile_list = b64decode("RnJlZWRvbSBGbG90aWxsYSxSZXNpc3RhbmNlLExpYmVyYXRpb24sRnJlZSBQYWxlc3RpbmUsR2F6YSxDZWFzZWZpcmUsUHJvdGVzdCxVTlJXQQ==").decode().split(',')

    @staticmethod
    def count_words(text, target_list):
        text = text.lower()
        text_list = text.lower().split()
        count_hostile = 0
        for word in target_list:
            word = word.strip().lower()
            if " " in word:
                count_hostile += text.count(word)
            else:
                count_hostile += text_list.count(word)
        return count_hostile

    def hostile_score(self,text):
        if not text or len(text.strip()) == 0:
            return 0
        count_hostile = self.count_words(text,self.list_hostile) * 2
        count_less_hostile = self.count_words(text,self.less_hostile_list)
        score = ((count_hostile + count_less_hostile) / len(text.split())) * 100
        self.logger.info("The hazard percentage calculation was successful.")
        return score

    def criminal_event(self,score):
        self.logger.info("Determination of criminality")
        return score > 6

    def danger_levels(self,score):
        self.logger.info("The danger level calculation was successful.")
        if score <= 5:
            return "none"
        elif score <= 15:
            return "medium"
        return "high"


    def menage_calculation(self,object_data):
        text = object_data.get('text')
        bds_percen = self.hostile_score(text)
        is_bds = self.criminal_event(bds_percen)
        bds_threat_level = self.danger_levels(bds_percen)
        object_data['bds_percen'] = bds_percen
        object_data['is_bds'] = is_bds
        object_data['bds_threat_level'] = bds_threat_level
        return object_data

