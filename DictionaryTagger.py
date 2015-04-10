__author__ = 'shrivas'
import yaml
class DictionaryTagger(object):
    def __init__(self, dictionary_paths):
        files = [open(path, 'r') for path in dictionary_paths]
        print(files);
        for dict_file in files:
            self.dictionaries = yaml.load(dict_file)



    # def tag_sentence(self, sentence, tag_with_lemmas=False):
    #     """
    #     the result is only one tagging of all the possible ones.
    #     The resulting tagging is determined by these two priority rules:
    #         - longest matches have higher priority
    #         - search is made from left to right
    #     """
    #     tag_sentence = []
    #     N = len(sentence)
    #     if self.max_key_size == 0:
    #         self.max_key_size = N
    #     i = 0
    #     while (i < N):
    #         j = min(i + self.max_key_size, N) #avoid overflow
    #         tagged = False
    #         while (j > i):
    #             expression_form = ' '.join([word[0] for word in sentence[i:j]]).lower()
    #             expression_lemma = ' '.join([word[1] for word in sentence[i:j]]).lower()
    #             if tag_with_lemmas:
    #                 literal = expression_lemma
    #             else:
    #                 literal = expression_form
    #             if literal in self.dictionary:
    #                 #self.logger.debug("found: %s" % literal)
    #                 is_single_token = j - i == 1
    #                 original_position = i
    #                 i = j
    #                 taggings = [tag for tag in self.dictionary[literal]]
    #                 tagged_expression = (expression_form, expression_lemma, taggings)
    #                 if is_single_token: #if the tagged literal is a single token, conserve its previous taggings:
    #                     original_token_tagging = sentence[original_position][2]
    #                     tagged_expression[2].extend(original_token_tagging)
    #                 tag_sentence.append(tagged_expression)
    #                 tagged = True
    #             else:
    #                 j = j - 1
    #         if not tagged:
    #             tag_sentence.append(sentence[i])
    #             i += 1
    #     return tag_sentence


contentArray =['Starbucks is not doing very well lately.',
               'Overall, while it may seem there is already a Starbucks on every corner, Starbucks still has a lot of room to grow.',
               'They just began expansion into food products, which has been going quite well so far for them.',
               'I can attest that my own expenditure when going to Starbucks has increased, in lieu of these food products.',
               'Starbucks is also indeed expanding their number of stores as well.',
               'Starbucks still sees strong sales growth here in the united states, and intends to actually continue increasing this.',
               'Starbucks also has one of the more successful loyalty programs, which accounts for 30%  of all transactions being loyalty-program-based.',
               'As if news could not get any more positive for the company, Brazilian weather has become ideal for producing coffee beans.',
               'Brazil is the world\'s #1 coffee producer, the source of about 1/3rd of the entire world\'s supply!',
               'Given the dry weather, coffee farmers have amped up production, to take as much of an advantage as possible with the dry weather.',
               'Increase in supply... well you know the rules...',]



dicttagger =  DictionaryTagger([ '/users/shrivas/Desktop/positive.yml', '/users/shrivas/Desktop/negative.yml'])


