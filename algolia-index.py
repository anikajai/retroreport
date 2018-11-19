from algoliasearch import algoliasearch
import yaml


client = algoliasearch.Client("M54GQ5QA25", "c7f4f469d460e8168e7012952d335a8b")
index = client.init_index("predemo_usc_index")

fileHandle = open("source.json")

items = yaml.load(fileHandle)
index.add_objects(items)

# index.setSettings({
#   'attributesToHighlight': [
#     'abstract',
#       'tags',
#       'title'
#   ]
# });

# index.batch_synonyms([{"objectID": "sRR0", "type": "synonym", "synonyms": ['longer', 'less', 'long', 'sooner', 'shorter', 'longer']},{"objectID": "sRR1", "type": "synonym", "synonyms": ['interesting', 'instructive', 'exciting', 'intriguing', 'fascinating', 'interesting']},{"objectID": "sRR2", "type": "synonym", "synonyms": ['binded', 'forming', 'shape', 'formation', 'forms', 'form']},{"objectID": "sRR3", "type": "synonym", "synonyms": ['gambling', 'casino', 'gamblers', 'gaming', 'casinos', 'gambling']},{"objectID": "sRR4", "type": "synonym", "synonyms": ['contests', 'matches', 'game', 'matchups', 'seasons', 'games']},{"objectID": "sRR5", "type": "synonym", "synonyms": ['videos', 'video', 'footage', 'clips', 'videotape', 'video']},{"objectID": "sRR6", "type": "synonym", "synonyms": ['evermore', 'increasingly', 'growingly', 'decreasingly', 'particularly', 'increasingly']},{"objectID": "sRR7", "type": "synonym", "synonyms": ['imagined', 'ever', "'ve", 'arguably', 'never', 'ever']},{"objectID": "sRR8", "type": "synonym", "synonyms": ['really', 'maybe', 'weird', 'kind', 'crazy', 'like']},{"objectID": "sRR9", "type": "synonym", "synonyms": ['track', 'racetrack', 'levigated', 'cuppy', 'tracks', 'track']},{"objectID": "sRR10", "type": "synonym", "synonyms": ['tailored', 'tailor', 'tailoring', 'tailors', 'customize', 'tailor']},{"objectID": "sRR11", "type": "synonym", "synonyms": ['became', 'become', 'becomes', 'becoming', 'become']},{"objectID": "sRR12", "type": "synonym", "synonyms": ['though', 'perhaps', 'if', 'actually', 'anyway', 'even']},{"objectID": "sRR13", "type": "synonym", "synonyms": ['music', 'entertainment', 'amusements', 'entertainments', 'multimedia', 'entertainment']},{"objectID": "sRR14", "type": "synonym", "synonyms": ['predominant', 'dominating', 'dominate', 'dominance', 'dominated', 'dominant']},{"objectID": "sRR15", "type": "synonym", "synonyms": ['keeps', 'stay', 'keeping', 'kept', 'keep']},{"objectID": "sRR16", "type": "synonym", "synonyms": ['expenditures', 'budgets', 'outlays', 'spending', 'expenditure', 'spending']},{"objectID": "sRR17", "type": "synonym", "synonyms": ['individuals', 'americans', 'folks', 'people', 'citizens', 'people']},{"objectID": "sRR18", "type": "synonym", "synonyms": ['fifty', 'decade', 'centuries', 'decades', 'century']},{"objectID": "sRR19", "type": "synonym", "synonyms": ['trying', 'looking', 'hoping', 'look', 'searching', 'looking']},{"objectID": "sRR20", "type": "synonym", "synonyms": ['day', 'moment', 'days', 'period', 'periods', 'time']},{"objectID": "sRR21", "type": "synonym", "synonyms": ['cash', 'funds', 'moneys', 'dollars', 'monies', 'money']},{"objectID": "sRR22", "type": "synonym", "synonyms": ['played', 'playing', 'play', 'game', 'plays', 'playing']},{"objectID": "sRR23", "type": "synonym", "synonyms": ['memories', 'anecdotes', 'perspectives', 'experience', 'stories', 'experiences']},{"objectID": "sRR24", "type": "synonym", "synonyms": ['games', 'play', 'match', 'matchup', 'ballgame', 'game']},{"objectID": "sRR25", "type": "synonym", "synonyms": ['artistically', 'choreographic', 'creative', 'artistic', 'musical', 'artistic']},{"objectID": "sRR26", "type": "synonym", "synonyms": ['interactivity', 'interactive', '3d', 'immerses', 'immersive', 'immersive']},{"objectID": "sRR27", "type": "synonym", "synonyms": ['developer', 'devs', 'developers', 'builders', 'developers']},{"objectID": "sRR28", "type": "synonym", "synonyms": ['behavior', 'habits', 'behaviors', 'misbehavior', 'behaviour', 'behavior']},{"objectID": "sRR29", "type": "synonym", "synonyms": ['playmaker', 'players', 'scorer', 'player', 'athlete', 'player']},{"objectID": "sRR30", "type": "synonym", "synonyms": ['prospects', 'current', 'upcoming', 'potential', 'future', 'future']},{"objectID": "sRR31", "type": "synonym", "synonyms": ['poker', 'gambling', 'casino', 'gaming', 'casinos', 'gaming']},{"objectID": "sRR32", "type": "synonym", "synonyms": ['became', 'become', 'becoming', 'makes', 'emerges', 'becomes']},{"objectID": "sRR33", "type": "synonym", "synonyms": ['promises', 'promising', 'promise', 'promised', 'encouraging', 'promising']},{"objectID": "sRR34", "type": "synonym", "synonyms": ['treatments', 'treatment', 'therapy', 'treating', 'therapies', 'treatment']},{"objectID": "sRR35", "type": "synonym", "synonyms": ['straightforward', 'simplest', 'simple', 'easy', 'uncomplicated', 'simple']},{"objectID": "sRR36", "type": "synonym", "synonyms": ['although', 'not', 'already', 'though', 'but', 'yet']},{"objectID": "sRR37", "type": "synonym", "synonyms": ['yesterday', 'tomorrow', 'monday', 'thursday', 'wednesday', 'today']},{"objectID": "sRR38", "type": "synonym", "synonyms": ['homicide', 'suicides', 'suicide', 'suicidal', 'sucide', 'suicide']},{"objectID": "sRR39", "type": "synonym", "synonyms": ['continues', 'continued', 'continuing', 'will', 'continue', 'continues']},{"objectID": "sRR40", "type": "synonym", "synonyms": ['explore', 'exploring', 'explored', 'examine', 'explore']},{"objectID": "sRR41", "type": "synonym", "synonyms": ['remarkably', 'shockingly', 'disappointingly', 'suprisingly', 'amazingly', 'surprisingly']},{"objectID": "sRR42", "type": "synonym", "synonyms": ['jeff', 'williams', 'bryan', 'armstrong', 'carter', 'jerry']},{"objectID": "sRR43", "type": "synonym", "synonyms": ['pandemic', 'outbreak', 'scourge', 'epidemics', 'epidemic', 'epidemic']},{"objectID": "sRR44", "type": "synonym", "synonyms": ['confronts', 'confronting', 'grapple', 'confronted', 'confront']},{"objectID": "sRR45", "type": "synonym", "synonyms": ['america', 'continent', 'national', 'country', 'world', 'nation']},{"objectID": "sRR46", "type": "synonym", "synonyms": ['implemented', 'instituted', 'implementation', 'implementing', 'implement', 'implemented']},{"objectID": "sRR47", "type": "synonym", "synonyms": ['downturn', 'meltdown', 'turmoil', 'crises', 'recession', 'crisis']},{"objectID": "sRR48", "type": "synonym", "synonyms": ['michael', 'audi', 'tr', 'alan', 'mr', 'dr']},{"objectID": "sRR49", "type": "synonym", "synonyms": ['invented', 'popularized', 'pioneering', 'revolutionized', 'pioneer', 'pioneered']},{"objectID": "sRR50", "type": "synonym", "synonyms": ['vets', 'servicemen', 'veteran', 'veterans', 'veterans']},{"objectID": "sRR51", "type": "synonym", "synonyms": ['fighting', 'combating', 'combats', 'combat', 'marines', 'combat']},{"objectID": "sRR52", "type": "synonym", "synonyms": ['techniques', 'methods', 'technique', 'methodology', 'tactic', 'method']},{"objectID": "sRR53", "type": "synonym", "synonyms": ['successful', 'succesful', 'success', 'successfull', 'fruitful', 'successful']},{"objectID": "sRR54", "type": "synonym", "synonyms": ['suggestion', 'theory', 'notion', 'ideas', 'concept', 'idea']},{"objectID": "sRR55", "type": "synonym", "synonyms": ['trying', 'attempting', 'hoping', 'tried', 'try', 'trying']},{"objectID": "sRR56", "type": "synonym", "synonyms": ['working', 'works', 'job', 'worked', 'work', 'work']},{"objectID": "sRR57", "type": "synonym", "synonyms": ['credo', 'mottos', 'slogan', 'mantra', 'mottoes', 'motto']},{"objectID": "sRR58", "type": "synonym", "synonyms": ['notoriety', 'attention', 'attentions', 'spotlight', 'acclaim', 'attention']},{"objectID": "sRR59", "type": "synonym", "synonyms": ['freshwater', 'water', 'sewage', 'groundwater', 'potable', 'water']},{"objectID": "sRR60", "type": "synonym", "synonyms": ['start', 'begin', 'starting', 'began', 'begins', 'beginning']},{"objectID": "sRR61", "type": "synonym", "synonyms": ['would', 'may', 'might', 'could', 'should', 'might']},{"objectID": "sRR62", "type": "synonym", "synonyms": ['drink', 'drunk', 'drank', 'drinking', 'imbibing', 'drinking']},{"objectID": "sRR63", "type": "synonym", "synonyms": ['scarcities', 'scarcity', 'dearth', 'shortage', 'shortages', 'scarcity']},{"objectID": "sRR64", "type": "synonym", "synonyms": ['earths', 'planet', 'earth', 'mankind', 'cosmos', 'earth']},{"objectID": "sRR65", "type": "synonym", "synonyms": ['can', 'might', 'will', 'could', 'should', 'may']},{"objectID": "sRR66", "type": "synonym", "synonyms": ['captured', 'capturing', 'captures', 'recapture', 'capture']},{"objectID": "sRR67", "type": "synonym", "synonyms": ['three', 'only', 'two', 'four', 'five', 'one']},{"objectID": "sRR68", "type": "synonym", "synonyms": ['locations', 'spots', 'place', 'locales', 'areas', 'places']},{"objectID": "sRR69", "type": "synonym", "synonyms": ['take', 'holds', 'holding', 'hold', 'held', 'hold']},{"objectID": "sRR70", "type": "synonym", "synonyms": ['solve', 'solutions', 'solves', 'solution', 'scalable', 'solution']},{"objectID": "sRR71", "type": "synonym", "synonyms": ['warmest', 'wettest', 'snowiest', 'soggiest', 'rainiest', 'driest']},{"objectID": "sRR72", "type": "synonym", "synonyms": ['crucial', 'vital', 'pivotal', 'critical', 'important', 'key']},{"objectID": "sRR73", "type": "synonym", "synonyms": ['inventive', 'innovations', 'innovator', 'innovating', 'innovation', 'innovative']}],forward_to_replicas=True, replace_existing_synonyms=True)
 # index.batch_synonyms([{
#     'objectID': 's3',
#     'type': 'synonym',
#     'synonyms': ['virulent', 'sulfurous', 'bitingly', 'taste', 'acerbic', 'gustatory_sensation', 'change_taste', 'ale', 'vitriolic', 'piercingly', 'sulphurous', 'taste_perception', 'acrid', 'bitterly', 'bitter', 'acid', 'acerb', 'acrimonious', 'bitterness', 'caustic']
#   },{
#     'objectID': 's4',
#     'type': 'synonym',
#     'synonyms':['blistering', 'taste_sensation', 'biting', 'taste_property', 'gustatory_perception', 'bitter']
#   }],
#   forward_to_replicas=True,
#   replace_existing_synonyms=True
# )
res = index.search(
    "supreme",
    {"attributesToRetrieve": "abstract, title, tag ", "hitsPerPage": 20}
)
#
print(res)