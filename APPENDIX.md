## More / extended examples

### Wrong to right

#### ID 2
```
Context:
1: Kentucky Jones
Kentucky Jones is a half-hour comedy/drama starring Dennis Weaver as Kenneth Yarborough "K.Y. or Kentucky" Jones, D.V.M., a recently widowed former horse trainer and active horse farm owner, who becomes the guardian of Dwight Eisenhower "Ike" Wong, a 10-year-old Chinese orphan, played by Ricky Der. Harry Morgan, previously of the CBS sitcoms "December Bride" and "Pete and Gladys", was featured in the series as Seldom Jackson, a former jockey who assists Dr. Jones. Cherylene Lee appears as Annie Ng, Ike's friend. Arthur Wong portrays Mr. Ng, Annie's father. Keye Luke (1904-1991) stars as Mr. Wong, a friend of Dr. Jones. Nancy Rennick (1932-2006) appears as Miss Throncroft, a social worker. "Kentucky Jones", which ran on NBC from September 19, 1964, to September 11, 1965, was the first of four television series starring Weaver after he left the role of the marshall's helper Chester Goode on CBS's western classic "Gunsmoke".
2: Harry Morgan
Harry Morgan (born Harry Bratsberg, April 10, 1915 – December 7, 2011) was an American actor and director whose television and film career spanned six decades. Morgan's major roles included Pete Porter in both "December Bride" (1954–1959) and "Pete and Gladys" (1960–1962); Officer Bill Gannon on "Dragnet" (1967–1970); Amos Coogan on "Hec Ramsey" (1972–1974); and his starring role as Colonel Sherman T. Potter in "MAS*H" (1975–1983) and "AfterMASH" (1983–1984). Morgan appeared in more than 100 films.

Question:
What is the reverse order of the letters in the first name of the role the actor who played Colonel Sherman T. Potter in "MAS*H" played in "Kentucky Jones"?
```

Base ❌:
```
<answer>yraH</answer>
```

CoT ✅:
```
The actor who played Colonel Sherman T. Potter in "MAS*H" is Harry Morgan. In "Kentucky Jones," he played the role of Seldom Jackson. The first name of that role is Seldom. Reversing the letters gives us "modleS."

<answer>modleS</answer>
```

Similar to the previous example, CoT provided a proper multihop reasoning to get the correct answer while Base did not.


### Both wrong
#### ID 3
```
Context:
1: Khyentse Norbu
Dzongsar Jamyang Khyentse Rinpoche (རྫོང་གསར་འཇམ་དབྱངས་མཁྱེན་བརྩེ་རིན་པོ་ཆེ།, born June 18, 1961), also known as Khyentse Norbu, is a Tibetan/Bhutanese lama, filmmaker, and writer. His four major films are "The Cup" (1999), "Travellers and Magicians" (2003), (2013) and, most recently, "Hema Hema: Sing Me a Song While I Wait" (2017). He is the author of the books "What Makes You Not a Buddhist" (Shambhala, 2007); "Not for Happiness: A Guide to the So-Called Preliminary Practices" (Shambhala, 2012); "The Guru Drinks Bourbon" (Shambhala, 2016); and "Best Foot Forward: A Pilgrim's Guide to the Sacred Sites of the Buddha" (Shambhala, 2018) and his other books like "Teachings on NgöndroParting from the Four AttachmentsWhat to do at India's Buddhist Holy SitesBuddha NatureIntroduction to the Middle Way" are also available through the Siddharthas Intent website. He is the eldest son of Thinley Norbu, and therefore the grandson of Dudjom Jigdral Yeshe Dorje. Rinpoche has teachers from all four major schools of Tibetan Buddhism and is a follower and champion of the Rimé (non-sectarian) movement. He considers Dilgo Khyentse as his main guru. He is also the primary custodian of the teachings of Jamyang Khyentse Wangpo.
2: The Cup (1999 film)
The Cup (ཕོར་པ། or "Phörpa") is a 1999 Tibetan-language film directed by Khyentse Norbu. The plot involves two young football-crazed Tibetan refugee novice monks in a remote Himalayan monastery in India who desperately try to obtain a television for the monastery to watch the 1998 World Cup final. The movie was shot in the Tibetan refugee village Bir in India (Himachal Pradesh) (almost entirely between Chokling Gompa and Elu Road). Producer Jeremy Thomas had developed a relationship with Norbu when he was an advisor on Bertolucci's "Little Buddha". Thomas later remembered his experience making the film:

Question:
What is the binary code of the last letter of the first name of the father of the director of film The Cup (1999 Film) in lowercase?
```

Base ❌:
```
<answer>1101110</answer>
```

CoT ❌:
```
The father of Khyentse Norbu is Thinley Norbu. The last letter of the first name "Thinley" is "y". In binary code, "y" in lowercase is represented as 01111001.

<answer>01111001</answer>
```



### Both right
#### ID 4
```
Context:
1: Alexander Leslie, Earl of Ross
Alexander Leslie, Earl of Ross( died 1402) was a Scottish nobleman. Born between 1367 and 1382, he was the son of Walter Leslie, Lord of Ross and Euphemia I, Countess of Ross. In around 1394 he became Earl of Ross and sometime before 1398 he married Isabel Stewart, daughter of Robert Stewart, Duke of Albany. They had one child, Euphemia. He died at Dingwall, Scotland on 8 May 1402.
2: Euphemia II, Countess of Ross
Euphemia II, Countess of Ross( also Euphemia Leslie) was the daughter of Alexander Leslie, Earl of Ross and his wife Isabella Stewart, daughter of Robert Stewart, 1st Duke of Albany. She was the only child and heir of Earl Alexander, and succeeded to the earldom" de jure" upon his death in 1402. She became a ward of her grandfather Albany, and never seems to have exercised much power in the province of Ross. There was a failed attempt to marry her to Thomas Dunbar, the son of Thomas Dunbar, Earl of Moray. Governor Albany persuaded her to resign the earldom to his own second son, John Stewart, Earl of Buchan. This action was challenged by Domhnall of Islay, Lord of the Isles, who claimed the earldom on behalf of his wife Mariota and who became an enemy of the Albany Stewarts. Euphemia thereafter disappears from the record, retiring to the nunnery of North Berwick. Some of the histories report that she was deformed, seemingly a hunchback.

Question:
How many fewer letters does the first name of Myra Bailey have compared to the first name of the paternal grandfather of Euphemia Ii, Countess Of Ross?
```

CoT ✅:
```
1. The first name of Myra Bailey is "Myra," which has 4 letters.
2. The paternal grandfather of Euphemia II, Countess of Ross, is Walter Leslie. The first name "Walter" has 6 letters.
3. To find how many fewer letters "Myra" has compared to "Walter," we calculate: 6 - 4 = 2.

<answer>2</answer>
```

while base directly answered 2