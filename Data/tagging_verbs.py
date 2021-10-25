from os import sep
import pandas as pd
from spacy_ditcs import LANGUAGE_DICTS



def get_verbs(data, lang, indexes, lang_dict):
    data_copy = data[ data["language"] == lang ]

    lang_indexes = []

    for i in data_copy.index:
        token = data_copy["translation"][i].split()[0]
        #print(token)
        pos = lang_dict(str(token))[0].pos_
        if "VERB" in pos:
            indexes.append(i)
            lang_indexes.append(i)
    print("Instances for "+ lang+":", len(lang_indexes))
    return indexes

def get_all_verbs(data, LANGUAGE_DICTS):

    indexes = []
    for lang in LANGUAGE_DICTS:
        lang_dict = LANGUAGE_DICTS[lang]
        indexes = get_verbs(data, lang, indexes, lang_dict)
    return indexes

def dropping_ge_imperives(data):
    indexes = []
    data_copy = data[data["language"] == "de"]
    for i in data_copy.index:
        if "Sie" in data_copy["translation"][i]:
            indexes.append(i)

    data.drop(indexes, inplace=True)
    return data

def removing_ACE_translations(data):

    data_copy = data[data["original"] == "ACE achieving competitive excellence"]
    data.drop(data_copy.index, inplace=True)
    return data


if __name__ == "__main__":

    clean_skills = pd.read_csv('Data/clean_skills.tsv', sep='\t')
    knowledge_concepts = pd.read_csv('Data/knowledge_concepts_pts.tsv', sep='\t')["uri"].to_list()

    print(clean_skills.shape)
    clean_skills_copy = clean_skills[ clean_skills["uri"].isin(knowledge_concepts) ]
    print(clean_skills_copy.shape)

    indexes = get_all_verbs(clean_skills_copy, LANGUAGE_DICTS)
    print(len(indexes))
    clean_skills.drop(indexes, inplace=True)
    print(clean_skills.shape)
    clean_skills = dropping_ge_imperives(clean_skills)
    print(clean_skills.shape)
    clean_skills = removing_ACE_translations(clean_skills)
    print(clean_skills.shape)
    clean_skills.reset_index(inplace=True)
    clean_skills.to_csv("Data/clean_skills_verbs.tsv", sep='\t', index=False)