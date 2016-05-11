# Notes

TODO:

### NOW
* migration to python3
* make init script nicer for someone else to use
* tests for learning.py - v important
* Actual experiments - normalising waveform intensity, more variation on the MLP experiment


### LATER
* produce a graph at the end for the test data
* Dockerise so others can easily develop (no real way of testing with scientific python packages with travis at the moment, unless docker is used)
* Turn TODO list into github issues

### Would be Cool
* make the fpython stuff nicer to use (currently in the bin folder of env, setup needs to add it to the folder)
* think of ways of making the experiments even more lightweight


## The Non-vocal baseline:
* 2 methods - spectrograms and raw waveform.

##  File Naming

files from new corpora will be changed to new names:

```
<subjectid>_<emotion>_<action>_<repitionid>

```
where:
* `subjectid` can be any string, so long as it is unique from ALL other files (incl. ones from other corpora).
* `emotion` is any from `{neutral, calm, happy, sad, angry, fearful, disgust, surprised}`
* `action` is a string representing what the subject is saying
* `repitionid` (optional) should be a number signifying if the subject has more than one recording of a specific emotion.

## Datasets That Look Useful:

* [RML emotion database](http://www.rml.ryerson.ca/rml-emotion-database.html): promising, although maybe a bit small, could go well with another corpus.

* [Montreal affected voices corpus](http://www.ncbi.nlm.nih.gov/pubmed/18522064): emotional vocalizations (laughing, crying etc.)

* [Italian affected voices corpus](http://www.lrec-conf.org/proceedings/lrec2014/pdf/591_Paper.pdf)

* [Toronto Emotional Speech Set](https://tspace.library.utoronto.ca/handle/1807/24487/browse?type=title&submit_browse=Title):

* [Berlin Emotional Speech Database](http://emotion-research.net/Members/AstridPaeschke/EmoDB):

* [RAVDESS](http://smartlaboratory.org/ravdess/): Currently in use

#### The ones below I looked at, but were not useful

* [buckeye corpus](http://buckeyecorpus.osu.edu/): Long conversations of
american english - not much metadata

* [voxforge](http://www.voxforge.org/): Lots of recordings, none of it about
the users emotions/stress levels, therefore likely not to have much range.

*   [Santa Barbara Corpus of Spoken American
English](http://www.linguistics.ucsb.edu/research/santa-barbara-corpus):
detailed but with no stress/emotion.

*   [Spoken Language Corpora at the Research Center on
Multilingualism](http://www.corpora.uni-hamburg.de/sfb538/en_overview.html):
same as the UCSB

*   [The Spoken Turkish Corpus at METU Ankara](http://std.metu.edu.tr/en/): Also normal corpus

*   [Spoken Corpus Klient with the Corp-Oral Corpus at ILTEC
Lisbon](http://www.iltec.pt/spock/)

*   [OLAC: Open Language Archives
Community](http://www.language-archives.org/)

*   [BAS Bavarian Archive for Speech
Signals](http://www.phonetik.uni-muenchen.de/Bas/BasHomeeng.html)

*   [Simmortel Speech Recognition Corpus for Indian English and
Hindi](http://www.simmortel.com/speech-recognition-corpus/)

*   [ELRA: the European Language Resources Association](http://www.elra.info/)

*   [The PELCRA Conversational Corpus of Polish](http://spokes.clarin-pl.eu/)