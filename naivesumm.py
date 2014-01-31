#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
A naive summarization approach based on Luhn1958 work
"The Automatic Creation of Literature Abstracts"
It uses the frequencies of words in the document in order to 
calculate and extract the sentences that include the most frequent words.

"""

# Copyright (C) 2012 Alejandro Mosquera <amsqr2@gmail.com>
 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist 
from nltk.corpus import stopwords


class NaiveSummarizer:
        def summarize(self, input, num_sentences ):
                punctuation = ['.',',','!','?']
                summ_sentences = []

                sentences = sent_tokenize(input)
                lowercase_sentences = [sentence.lower()for sentence in sentences]
                #print lowercase_sentences
                
                s = list(input)
                ts = ''.join([ o for o in s if not o in  punctuation ]).split()
                lowercase_words = [word.lower() for word in ts]
                words = [word for word in lowercase_words if word not in stopwords.words()]
                word_frequencies = FreqDist(words)

                most_frequent_words = [pair[0] for pair in word_frequencies.items()[:100]]

                # add sentences with the most frequent words
                for word in most_frequent_words:
                        for i in range(0, len(lowercase_sentences)):
                                if len(summ_sentences) < num_sentences:
                                        if (lowercase_sentences[i] not in summ_sentences and word in lowercase_sentences[i]):
                                                summ_sentences.append(sentences[i])
                                                break

                                                
                # reorder the selected sentences
                summ_sentences.sort( lambda s1, s2: input.find(s1) - input.find(s2) )
                return " ".join(summ_sentences)


if __name__ == "__main__":

    naivesum = NaiveSummarizer()
    text='''
    To see a world in a grain of sand,
    And a heaven in a wild flower,
    Hold infinity in the palm of your hand,
    And eternity in an hour.

    A robin redbreast in a cage
    Puts all heaven in a rage.

    A dove-house fill'd with doves and pigeons
    Shudders hell thro' all its regions.
    A dog starv'd at his master's gate
    Predicts the ruin of the state.

    A horse misused upon the road
    Calls to heaven for human blood.
    Each outcry of the hunted hare
    A fibre from the brain does tear.

    A skylark wounded in the wing,
    A cherubim does cease to sing.
    The game-cock clipt and arm'd for fight
    Does the rising sun affright.

    Every wolf's and lion's howl
    Raises from hell a human soul.

    The wild deer, wand'ring here and there,
    Keeps the human soul from care.
    The lamb misus'd breeds public strife,
    And yet forgives the butcher's knife.

    The bat that flits at close of eve
    Has left the brain that won't believe.
    The owl that calls upon the night
    Speaks the unbeliever's fright.

    He who shall hurt the little wren
    Shall never be belov'd by men.
    He who the ox to wrath has mov'd
    Shall never be by woman lov'd.

    The wanton boy that kills the fly
    Shall feel the spider's enmity.
    He who torments the chafer's sprite
    Weaves a bower in endless night.

    The caterpillar on the leaf
    Repeats to thee thy mother's grief.
    Kill not the moth nor butterfly,
    For the last judgement draweth nigh.

    He who shall train the horse to war
    Shall never pass the polar bar.
    The beggar's dog and widow's cat,
    Feed them and thou wilt grow fat.

    The gnat that sings his summer's song
    Poison gets from slander's tongue.
    The poison of the snake and newt
    Is the sweat of envy's foot.

    The poison of the honey bee
    Is the artist's jealousy.

    The prince's robes and beggar's rags
    Are toadstools on the miser's bags.
    A truth that's told with bad intent
    Beats all the lies you can invent.

    It is right it should be so;
    Man was made for joy and woe;
    And when this we rightly know,
    Thro' the world we safely go.

    Joy and woe are woven fine,
    A clothing for the soul divine.
    Under every grief and pine
    Runs a joy with silken twine.

    The babe is more than swaddling bands;
    Every farmer understands.
    Every tear from every eye
    Becomes a babe in eternity;

    This is caught by females bright,
    And return'd to its own delight.
    The bleat, the bark, bellow, and roar,
    Are waves that beat on heaven's shore.

    The babe that weeps the rod beneath
    Writes revenge in realms of death.
    The beggar's rags, fluttering in air,
    Does to rags the heavens tear.

    The soldier, arm'd with sword and gun,
    Palsied strikes the summer's sun.
    The poor man's farthing is worth more
    Than all the gold on Afric's shore.

    One mite wrung from the lab'rer's hands
    Shall buy and sell the miser's lands;
    Or, if protected from on high,
    Does that whole nation sell and buy.

    He who mocks the infant's faith
    Shall be mock'd in age and death.
    He who shall teach the child to doubt
    The rotting grave shall ne'er get out.

    He who respects the infant's faith
    Triumphs over hell and death.
    The child's toys and the old man's reasons
    Are the fruits of the two seasons.

    The questioner, who sits so sly,
    Shall never know how to reply.
    He who replies to words of doubt
    Doth put the light of knowledge out.

    The strongest poison ever known
    Came from Caesar's laurel crown.
    Nought can deform the human race
    Like to the armour's iron brace.

    When gold and gems adorn the plow,
    To peaceful arts shall envy bow.
    A riddle, or the cricket's cry,
    Is to doubt a fit reply.

    The emmet's inch and eagle's mile
    Make lame philosophy to smile.
    He who doubts from what he sees
    Will ne'er believe, do what you please.

    If the sun and moon should doubt,
    They'd immediately go out.
    To be in a passion you good may do,
    But no good if a passion is in you.

    The whore and gambler, by the state
    Licensed, build that nation's fate.
    The harlot's cry from street to street
    Shall weave old England's winding-sheet.

    The winner's shout, the loser's curse,
    Dance before dead England's hearse.

    Every night and every morn
    Some to misery are born,
    Every morn and every night
    Some are born to sweet delight.

    Some are born to sweet delight,
    Some are born to endless night.

    We are led to believe a lie
    When we see not thro' the eye,
    Which was born in a night to perish in a night,
    When the soul slept in beams of light.

    God appears, and God is light,
    To those poor souls who dwell in night;
    But does a human form display
    To those who dwell in realms of day.
    '''

    print(naivesum.summarize(text,4))
