class Card(object):
    def __init__(self, identifier, expansion, name, cost, ad, hp, ms, attack_type, faction, card_class, race, effect):
        self.identifier = identifier
        self.expansion = expansion
        self.name = name
        self.cost = cost
        self.ad = ad
        self.hp = hp
        self.ms = ms
        self.attack_type = attack_type
        self.faction = faction
        self.card_class = card_class
        self.race = race
        self.effect = effect