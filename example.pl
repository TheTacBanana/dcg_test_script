% Sentence
s(s(NP,VP)) --> np(P, NP),vp(P, VP).

% Noun Phrase
np(P, np(Det,N))
    --> det(P, Det),
        n(P, N).

% Verb Phrase
vp(P, vp(V,NP))
    --> tv(P,V),
        np(_,NP).

% Determiner
det(Plurality, det(Word))
    --> [Word],
        {lex(Word,det,Plurality)}.

% Atomics
n(Plurality, n(Word)) --> [Word], {lex(Word,n,Plurality)}.
tv(Plurality, v(Word)) --> [Word], {lex(Word,tv,Plurality)}.
iv(Plurality, v(Word)) --> [Word], {lex(Word,iv,Plurality)}.

% Lexicon
lex(the, det, _).
lex(a, det, singular).
lex(two, det, plural).
lex(woman, n, singular).
lex(man, n, singular).
lex(women, n, plural).
lex(men, n, plural).
lex(hires, tv, singular).
lex(hire, tv, plural).