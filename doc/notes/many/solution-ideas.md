# Problem: "Many"

## Graf-versioner:
* _Grid_
    * Hvis N == 2: 
    * Vi kan ikke lave en path som inkluderer alle vertices. 
    * Derfor vil Many(G) = 1 (hvis *s* er rød) + 1 (hvis *t* er rød) + 1 (hvis der findes en rød der ikke er *s* eller *t*).
   * Alle andre tilfælde: 
    * Many(G) = |R|
* _Walls_
    * 1 edge overlap: 
    * Many(G) = 1
   * 0 edge overlap: 
    * Hvis *s* eller *t* (eller begge) er placeret på en node med 2 edges på samme mursten som den røde node så 1, ellers 0.
   * Negativt overlap: 
    * Samme svar som for "0 edge overlap".
* _Ski_
    * Dynamisk programmering 
   * Vi behøver kun 1 række cache/memory, længde N
   * Vi skal pre-process og lave en graf med inverted edges.
   * (Evt TA spg: Er det stadig målet at finde maks. antal røde, selvom det nu er onde Yeti?)
* _Increasing numbers_
    * Dynamisk programmering
   * Vi behøver kun 1 række cache/memory, længde N
   * Vi skal pre-process og lave en graf med inverted edges.

Adrian confirmed David's idea: We can solve some (not all) general scenarios by using Bellman-Ford (which allows cycles) and finding "shortest path" where edges to red nodes have weight -1 and all other edges have weight 0. It doesn't work for cycles with negative weight, though.