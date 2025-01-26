# A brief exploration on GPT 4o-mini's multihop reasoning with CoT
We explore the capabilities of GPT 4o-mini's multihop reasoning with and without CoT,
via the [Inspect](https://inspect.ai-safety-institute.org.uk/) framework 
on the [MorehopQA](https://github.com/Alab-NII/morehopqa/) dataset.

## Overview
This project evaluates GPT-4o-mini's performance on multi-hop reasoning tasks using the MorehopQA dataset. It compares performance with and without Chain-of-Thought (CoT) prompting using the Inspect framework for systematic evaluation on a subsample.

For code details and installation instructions, see [DETAILS.md](DETAILS.md)

## Methodology
We use the MorehopQA's [prompt template](https://github.com/Alab-NII/morehopqa/blob/main/models/prompt_generator.py) for both settings, which follow the format

```
You will be asked a question, and should provide a short answer.
If the answer is a date, format is as follows: YYYY-MM-DD (ISO standard)
If the answer is a name, format it as follows: Firstname Lastname
If the answer contains any number, format it as a number, not a word, and only output that number. Do not include leading 0s.

Please provide the answer in the following format: <answer>your answer here</answer>
Answer as short as possible.

Context:
{context}

Answer the following question:
{question}
```

For CoT, `Let's think step by step.` is added to the prompt.


## Analysis
Out of the 5 samples, 3 were answered correctly with CoT, and 1 was answered correctly without CoT.

### Summary

CoT significantly enhances multihop reasoning (or rather, multihop reasoning is hard without CoT).

Even when CoT got the answer wrong, it manages to provide the right (though incomplete) logic.

### Wrong to right
Questions where CoT made the difference:

#### ID 1
```
Context:
1: Maroon 5
Maroon 5 is an American pop rock band that originated in Los Angeles, California. It currently consists of lead vocalist Adam Levine, keyboardist and rhythm guitarist Jesse Carmichael, bassist Mickey Madden, lead guitarist James Valentine, drummer Matt Flynn and keyboardist PJ Morton.
2: What Lovers Do
"What Lovers Do" is a song by American pop rock band Maroon 5 featuring American R&B singer Sza. It was released on August 30, 2017, as the third single from the band's upcoming sixth studio album (2017). The song contains an interpolation of the 2016 song "Sexual" by Neiked featuring Dyo, therefore Victor Rådström, Dyo and Elina Stridh are credited as songwriters.

Question:
What is the ASCII code of the last letter of the first name of the current drummer of the band who did the song "What Lovers Do"?
```

Base ❌: 
```
<answer>110</answer>
```

CoT ✅:
```
The current drummer of Maroon 5 is Matt Flynn. The last letter of his first name "Matt" is "t". The ASCII code for "t" is 116.

<answer>116</answer>
```

Base did not provide any reasoning and just came up with a wrong answer while CoT properly did the multihop reasoning required to get the correct answer.

Another similar example is ID 2 in the [APPENDIX.md](APPENDIX.md).

### Both wrong
#### ID 3
(full example in [APPENDIX.md](APPENDIX.md))
```
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

The answer is in fact `1111001` which CoT **got right but did not format correctly** (remove leading 0s), whereas Base got it completely wrong (binary translates to the letter `n`).

#### ID 5
```
Context:
1: Chiang Hsiao-wu
Chiang Hsiao-wu (also known as Alex Chiang; April 25, 1945 - July 1, 1991) was the second son of Chiang Ching-kuo, the President of the Republic of China in Taiwan from 1978 to 1988. His mother is Faina Ipatyevna Vakhreva, also known as Chiang Fang-liang. He had one older brother, Hsiao-wen, one older sister, Hsiao-chang, and one younger brother, Hsiao-yung. He also had two half-brothers, Winston Chang and John Chiang, with whom he shared the same father. He was president of the state-run Broadcasting Corporation of China from 1980 to 1986, and later headed the Republic of China mission to Singapore for two years, starting in April 1986 as the deputy trade representative before being transferred to the mission to Japan in 1990. In a December 1985 speech, Hsiao-wu's father Chiang Ching-kuo declared ″If someone asks me whether anyone in my family would run for the next presidential term, my reply is, ′It can't be and it won't be.′″ Prior to the speech, Chiang Hsiao-wu was the only one of Chiang Ching-kuo's sons mentioned as a potential successor. He died at the age of 46, on July 1, 1991, at the Taipei Veterans General Hospital in Taiwan as a result of congestive heart failure brought on by chronic inflammation of the pancreas. He was survived by his wife and two children.
2: Chiang Ching-kuo
Chiang Ching-kuo (27 April 1910 – 13 January 1988) was a politician of the Republic of China. The eldest and only biological son of former president Chiang Kai-shek, he held numerous posts in the government of the Republic of China. He served as Premier of the Republic of China between 1972–78 and was the President of the Republic of China from 1978 until his death in 1988. Chiang Ching-kuo was sent as a teenager to study in the Soviet Union during the First United Front in 1925, when his father's Nationalist Party and the Chinese Communist Party were in alliance. He attended university there, but when the Chinese Nationalists violently broke with the Communists, Stalin sent him to work in a steel factory in the Ural Mountains. There he met and married Faina Vakhreva. When war between China and Japan was imminent in 1937, Stalin sent the couple to China. During the war his father gradually came to trust Ching-kuo and gave him more and more responsibilities, including administration. After the Japanese surrender, Chiang-kuo was given the job of ridding Shanghai of corruption, which he attacked with ruthless efficiency. The victory of the Communists in 1949 drove the Chiangs and their government to Taiwan. Chiang Ching-kuo was first given control of the secret police, a position he retained until 1965 and in which he used arbitrary arrests and torture to ensure tight control. He then became Minister of Defense 1965-1969, Vice-Premier, 1972-78, Premier, 1972-78. After his father's death in 1976 he took leadership of the Nationalist Party as Chairman, and was elected President of the Republic in 1978. Under his tenure, the government of the Republic of China, while authoritarian, became more open and tolerant of political dissent. Chiang courted Taiwanese voters and reduced the preference for those who had come from the mainland after the war. Towards the end of his life, Chiang relaxed government controls on the media and speech and allowed Taiwanese Han into positions of power, including his successor Lee Teng-hui.

Question:
How many fewer letters does the last name of Melvin Johns have compared to the first name of the paternal grandfather of Chiang Hsiao-Wu?
```

Base ❌:
```
<answer>2</answer>
```

CoT ❌:
```
First, we identify the paternal grandfather of Chiang Hsiao-wu, which is Chiang Kai-shek. His first name is "Kai-shek," which has 8 letters.

Next, we look for the last name of Melvin Johns, which is "Johns," having 5 letters.

Now, we calculate the difference in the number of letters:
8 (Kai-shek) - 5 (Johns) = 3.

Thus, the answer is:

<answer>3</answer>
```

CoT only made the mistake because it confused the first name of Chiang Kai-shek with his last name (due to reversal of first and last names in Asian names), but it's logic is right. It can be argued that from the passage, due to the presence of aliases ("Alex Chiang"), an additional reasoning step could have resolved the confusion.

Also, notice that the hop to the paternal grandfather's name missed a step.

On the other hand, Base's answer is completely off.

### Both right
#### ID 4
(full example in [APPENDIX.md](APPENDIX.md))
```
Question:

How many fewer letters does the first name of Myra Bailey have compared to the first name of the paternal grandfather of Euphemia Ii, Countess Of Ross?
```

This is a 3 hop question which surprisingly base got right
