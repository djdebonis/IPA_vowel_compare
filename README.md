# sla
Jupyter notebook running python code for comparative analysis of International Phonetic ALphabet (IPA) transcriptions.
The emphasis of this notebook (and the study that accompanies it) is vowel comparison.

## Program & notebook

The intention of this notebook is to perform contrastive data analysis between prescriptive and descriptive IPA strings. Although the original intention is IPA strings, many of the functions could likely be tweaked and extrapolated to other string comparisons, such as spell checking or DNA sequencing etc. (I really have no clue--like I said the intention was IPA strings.)

Along with the Jupyter notebook, there are also sample datasets in the repository. In the transcriptions/ directory are a set of IPA transcriptions taken from study-participant recordings (see **Current Study**) stored in text files. According to IPA guidelines, each word is separated with " # " to denote a pause in the speech. Prosodic accent marks (" ' ") are only attached to syllables (preceding the stressed syllable) in which the participant stressed *the incorrect* syllable. These transcriptions (or others like it) can be read into the notebook, cleaned by the functions, and then set against each other (or, in this case, against a prescriptive, 'correct,' transcription) for analysis.

There are also two .csv files, dictionary.csv and survey_data.csv. The former contains meta-information about the word-list sample and its linguistic properties, while the latter has responses to the survey that participants took before recording their pronunciation. Note that some of the functions are designed specifically for these datasets.

## Current Study

The current study was conducted as a final project for Spanish Applied Linguistics: Second Language Acquisition, a course @ The University of Colorado, Denver, taught by my professor & research advisor, Dra. Alyssa Martoccio.

### Basic methods

The current study is a pilot study examining materials & methods--specifically those related to the data calculation, analysis, & representation.

In the current study, participants were asked to read a list of 25 Spanish words. Participants were aware that the study was relating to pronunciation, but they were not instructed to focus on any specific component of their pronunciation. The list of 25 words is as follows: 

hice, combinación, inicio, educación, hasta, ojo, casi, usar, funcionar, cantar, ayuda, hombre, está, sabe, oportunidad, toque, él, su, hermana, esta, taza, importante, qué, el, tanto

This word list was transcribed to the International Phonetic Alphabet, or IPA, (see djdebonis/phonetics repo for more on transcription) according to prescriptive rules. Dialectical features were not accounted for in this study because (1) most dialectical variation is consonantal in Spanish, and (2) none of the participants were native or heritage speakers. The transcription is as follows:

i-se # kom-bi-na-si̯on # i-ni-si̯o # e-ðu-ka-si̯on # as-ta # o-ho # ka-si # u-saɾ # fun-si̯o-naɾ # kan-taɾ # a-ju-ða # om-bɾe # es-ta # sa-βe # o-poɾ-tu-ni-ðað # to-ke # el # su # eɾ-ma-na # es-ta # ta-sa # im-poɾ-tan-te # ke # el # tan-to

(this transcription is also stored in /transcriptions/rescriptive_ls.txt)

### Participants

Eight participants were selected by snowball sample (no randomization--all volunteers were included & elected). All of the participants filled out a survey with information about their experience with Spanish and Spanish-learning. After this, all of the participants were instructed to record themselves reading the aforementioned word list. All of the recordings were manually transcribed into IPA (see limitations).

### Vowels

In this word list, 59 vocalic environments were examined and analyzed. This is *not* to say there were only 59 total vowels in the study; instead, the vowels within each syllable were designated their own allophonic environment, and these environments were analyzed. (The reason for this is that the focus of the present study was on pure vowels, and the average Spanish word has only one vowel set; this vowel set may contain two vowels in the case of a diphthong, but they will be counted together for this experiment.) Only vowels sets were examined for accuraccy or 'correctness.' For example, if the prescriptive syllable in question was [te], then the student would have been deemed accurate for [te], or even [de], because the vowel set ([e]) matches that of the prescriptive. If the student, however, answered [tɛ] or [tei̯], their pronunciation would be marked inaccurate for that specific set.

Participants were asked to record themselves reading a list of 25 Spanish words. All participants were notified that the study's emphasis was on pronunciation, but no specifics were divulged. The word list was assembled with common-use Spanish words. The words were categorized according to three True/False criteria that evaluated their *phonemic/phonetic* quality: (1) is vowel-initial; (2) is terminal-vowel; and (3) is English cognate. Some of the words were assigned to more than one category. Out of the word set, a total of 15 words were vowel-intial, 17 words were terminal-vowel, and 6 words were cognates. The words were also assigned further with 'vowel focus/emphasis' categories: five of these categories focused on the five primary Spanish vowels: < a >, < e >, < i >, < o >, and < u >. The other two categories focused on: < h& >, where a vowel of the word was preceded by the letter < h >, which has no phonetic realiztion; and, < qu& > where a vowel was preceded by the letters < qu >, in which the letter < u > has no phonetic realization.

### Sample

In the sample (n = 8), the participants had recieved an average of 3.25 years of formal Spanish language instruction (SD = 2.5 years), with a range between 0 and 7 years (one year was defined as: a complete High School year, a College semester, or a relative equivalent). The participants, in total, scored an average of 78.39% accuracy in the pronunciation of *all of* the vowels (SD = 11.11%). The average accuracy of vowel pronunciation in cognates (words that share a similar origin--and thus appear similarly --between English and Spanish) was 77.85% (SD = 17.52%); surpsingly, the average accuracy of vowel pronunciation in non-cognates was very close, with an average of 78.72% (SD = 7.75). A 2-sample-t-test confirmed that there wasn't enough evidence to declare a statistically significant difference between the accuracy averages of cognates and non-cognates. This went against one of the inital hypotheses: that NESs would have less accuracy with cognates due to more explicit language transfer. 

### Results

As is mentioned, this was a pilot study who's focus was to explore materials, methods, and implications. Few results were drawn.


### Discussion

### Limitaitons

There were oh-so-many limitations to this study. The first and most prominent limitation is the sample size. It is very difficult--if not completely impossible--to draw conclusions about Spanish language aquisition with a sample size of 8 Spanish L2 learners. However, as was previously noted, this was a pilot study aimed at testing the materials & methods and examining potential analyzes that could be completed in future studies.

The second major limitation was that, for this study, I was the only researcher involved in transcribing the participant recordings into IPA. Although I have a lot of experience transcribing Spanish IPA and comparing my results with other researchers, there is an inherent subejctivity and bias of a single transcriber; problems can arise from both perception of sound and confirmation bias. Future studies should include multiple transcribers in a collaborative setting. (Future research should also examine machine learning of audio files to transcribe to IPA.)

A major limitation of the development of the materials--which was only realized *post hoc*--was the lack of a survey question that asked about other L1s or L2s that are not Spanish. I only realized this after a friend of mine completed the survey who's first language is Italian; speaking another Romance language as an L1 is a clear confounding variable that was not accounted for in this study.

Further, future studies must include more randomization in the sampling. A snowball sample works well enough for the purpose of the pilot study, but if conclusions are to be drawn it is important that there is randomization so that the sample is as representative as possible. 

Finally, this study was a completely correlational study that relied completely on past experiences to draw conclusions about factors influencing pronunciation. Future studies should examine factors relating to phonetic/phonemic aquisition in a controlled study. An example of this might be to examine the effect of explicit, contrastive instruction of phonetics compared against an implicit, audio-lingual repetition control, where both the explicit and implicit groups have exposure to similar quantities of target tokens.