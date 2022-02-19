# wordle-tr-helper

This repo contains a REST API which returns __5-letter words__ in Turkish.
It can easily be used for generating hints when playing _wordle-tr_.

## Input

Input format is as following:

```
{
    "word_arr": [
        "-", "-", "-", "-", "-"
    ],
    "word_rnd": []
}
```

The example above gives every word in the dictionary.

For the filtering, you can change attribute values as stated below.

### Input Fields

#### word_arr
This field is a required field and represents the 5-letter word. It accepts a String array which contains the letters in the indices.
For example, if you want to get words that started __s__ letter, you should use:

```
{
    "word_arr": [
        "s", "-", "-", "-", "-"
    ]
}
```

#### word_rnd
This field represents the letters which is in the word but the exact index isn't known.
For example, if your word is like __--ar-__ and also you know the letter __m__ in the word (and you don't know its place), you should use:
```
{
    "word_arr": [
        "-", "-", "a", "r", "-"
    ],
    
    "word_rnd": [ "m" ]
}
```

## Output
The API returns a list of Word objects which is in following format:

```
{
    "madde": <WORD_1>,
    "anlamlarListe": [
        {
            "anlam": <WORD_1_MEANING_1>
        },
        
        ...
        
        {
            "anlam": <WORD_1_MEANING_M>
        }
    ],
    
    ...
    
    "madde": <WORD_N>,
    "anlamlarListe": [
        {
            "anlam": <WORD_N_MEANING1>
        },
        
        ...
        
        {
            "anlam": <WORD_N_MEANING_M>
        }
    ]
}
```

For the example above (the one in _word_rnd_ topic), the sample output is:

```
[
    {
        "madde": "alarm",
        "anlamlarListe": [
            {
                "anlam": "Bir uyarıyı, bir tehlikeyi bildirmek için verilen işaret"
            },
            {
                "anlam": "Bu işareti veren düzenek"
            }
        ]
    },
    {
        "madde": "emare",
        "anlamlarListe": [
            {
                "anlam": "Belirti, iz, ipucu"
            }
        ]
    },
    {
        "madde": "muare",
        "anlamlarListe": [
            {
                "anlam": "Dalgalı parıltılar verilmiş olan bir kumaş türü, kareli kumaş"
            },
            {
                "anlam": "Bu kumaştan yapılan"
            }
        ]
    }
]
```

## Technical Details
This repo contains a REST API which has one endpoint. 
The API written in FastAPI library and the dataset places in MongoDB Atlas.

For executing the repo, just clone or download it and run the following command to serve it:

```
uvicorn main:app --reload
```

Before that, you should install the required libraries using following command:

```
pip install -r requirements.txt
```
