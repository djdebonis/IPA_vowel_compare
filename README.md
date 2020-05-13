# sla
Jupyter notebook running python code for comparative analysis of IPA transcriptions.
The emphasis of this notebook (and the study that accompanies it) is vowel comparison.

## Program & notebook

The intention of this notebook is to perform contrastive data analysis between prescriptive and descriptive IPA strings. Although the original intention is IPA strings, many of the functions could likely be tweaked and extrapolated to other string comparisons, such as spell checking or DNA sequencing etc. (I really have no clue--like I said the intention was IPA strings.)

Along with the Jupyter notebook, there are also sample datasets in the repository. In the transcriptions/ directory are a set of IPA transcriptions taken from study-participant recordings (see **Current Study**) stored in text files. According to IPA guidelines, each word is separated with " # " to denote a pause in the speech. Prosodic accent marks (" ' ") are only attached to syllables (preceding the stressed syllable) in which the participant stressed *the incorrect* syllable. These transcriptions (or others like it) can be read into the notebook, cleaned by the functions, and then set against each other (or, in this case, against a prescriptive, 'correct,' transcription) for analysis.

There are also two .csv files, dictionary.csv and survey_data.csv. The former contains meta-information about the word-list sample and its linguistic properties, while the latter has responses to the survey that participants took before recording their pronunciation. Note that some of the functions are designed specifically for these datasets.

## Current Study

The current study is a pilot study examining materials & methods--specifically those related to the data calculation, analysis, & representation.

In the current study 59 vocalic environments were examined and analyzed. This is *not* to say there were only 59 total vowels in the study; instead, the vowels within each syllable were designated their own allophonic environment, and these environments were analyzed. (The reason for this is that the focus of the present study was on pure vowels, and the average Spanish word has only one vowel set; this vowel set may contain two vowels in the case of a diphthong, but they will be counted together for this experiment.) Only vowels sets were examined for accuraccy or 'correctness.' For example, if the prescriptive syllable in question was [te], then the student would have been deemed accurate for [te], or even [de], because the vowel set ([e]) matches that of the prescriptive. If the student, however, answered [tɛ] or [tei̯], their pronunciation would be marked inaccurate for that specific set.

Participants were asked to record themselves reading a list of 25 Spanish words. All participants were notified that the study's emphasis was on pronunciation, but no specifics were divulged. The word list was assembled with common-use Spanish words. The words were categorized according to three True/False criteria that evaluated their *phonemic/phonetic* quality: (1) is vowel-initial; (2) is terminal-vowel; and (3) is English cognate. Some of the words were assigned to more than one category. Out of the word set, a total of 15 words were vowel-intial, 17 words were terminal-vowel, and 6 words were cognates. The words were also assigned further with 'vowel focus/emphasis' categories: five of these categories focused on the five primary Spanish vowels: < a >, < e >, < i >, < o >, and < u >. The other two categories focused on: < h& >, where a vowel of the word was preceded by the letter < h >, which has no phonetic realiztion; and, < qu& > where a vowel was preceded by the letters < qu >, in which the letter < u > has no phonetic realization.
