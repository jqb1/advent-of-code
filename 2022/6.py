with open("./input.txt") as f:
    moves = [line.rstrip() for line in f]

print(moves)

# test_input = """
# abc
# bbd
# """
# test_input = test_input.split("\n")[1:-1]
# print(test_input)
#
actual_input = """
plhlsssjsrscspsffmrffwvfvrvvmbbnjnrnrfnndlnlznlznlnccdbbhvbvgvmvzmzvmzmbbrcclsslzslzzsztzftzzhggnjgnjnhnmnqnqqfdfnnrwnwsnwwvgvqqgpptvtrvvfmmzjzmmjssmwsmmhzzvvwzwcwrcrllpbppdgdvvwqvvsnsrnsncnwntnggwqgqhqrqprqrddjvddqsqhshchfffzddswdsshhcnhnqqfjffvlvwvssdqqwrwvrvhrvrzzgwggcjcgclcwchhzvzmzrrjwjqwwvbwwrmmvmpmzpzgpgsghgrrtmmlfmmnzzmpzzvmvjjsqqshqshsqqgtqggpvvrtttwbbhnbnlbnlnhnthtjhjshhrmrjjlclpprmrnrsrwrbwrwwjnwnbwbhbmbggdbgghllcvlvddzbdbdvdwvdvjvqvcvczvcvclvvrggrngrrwcwbcczgghnhznhnttbcbvcvttrrpbrppndppvvvgvtgvvhfvhhttppjmjllznlnldnldlwlnwlnlttgzzcfcggwmgmqgmmshmhqqdfqfpfqppprzrhrnrhnrrtsrrgpgnpngnqnmmrtrvtrrfccszszffvlfvlvssvdvvpggvcvscvvpmpgpqpfqqhttrhhsbhbqhhzggzrgrqrfqffwllggrgqqjzqzzsgglvgllsgllptltblbggvrggctczzllvsvcscrrzjrzzjnnbvvtntpntnvtntcntcnnwsnnnvjnnsccsddcvvgzgwggbnbwnwbwmwttzzsgzzjpzztwztwwhhzggplgplggwwwphpmmhchsccmwmttvjtjftffzbfffjljbbqvvstsggbbqrbqrbrhbbrmbmppvrpphptpggqgddtmdtmdmbbbcdbbgssmzzthhtjjrgjrgrzzchzhttgddjnjrjmjllrcrqqsvsjjjhvvphhgjhgjhjccwmcmjcmjmhmzznmmcbcscddcsssnppsnpnmnqmmtztftqtjtqqgvgvjjfnjffqbqbfqqwfqfcfsfttvccnssjvvpfvpvttvpvccwhwfwlwlclljqqststllgqgzqqfpflpplpssnntstqqpnnsrnsrrsvrsvsrvsrrtztmtptpcpssgnnfvflffscsqszzsppfnftfptfpfnfbbwzbzfbbtggrzrnntztnznhnnlbnbrbdddjhjchhdshhnzhnnsrnrrqwrrdsdlsstdsslqsqdqvqzvqvwqqlmmwzmwzwztzlzczhqfrclvgvnlchrggsrjhntctdbpfdcffwjngdvdrjmgvwvptlvlhvhshqphmrdznqbtchcvrwfrpvwhzmrwlcjwnrsgrqcbsgpwjthstvqzlwjjmqbvhhdfdsmqnmnswmwjtpgjhdpgcnvmlcjwjzrjhmrqmqnrqrmgdnbdgznwhgzncmcbzpntcdflvrbfdzwgpnqjqmrcqpbrzwhwdgtgshhmrwvhnrwslvcswjvdgglfrdvmqdspppwmvfzvdbvpcnhmvgfqwnvjvvzrvttwvbjrbjlllmwtlcltvqmwshnqsdtjrptvqjvdjgzwgzzhcdbwjzhdgsptfrtmmqvhsnsnpgwbncbnnvwmmrrjgfccbzcpcjmqvqsbvjrstzblsrngphwndfdswjnnnfdgpcbslvbjglqqnbbtjljsmdgcslmwlvgwpsqthlmmqfgpgmcvrpvvtzcjdrwcjgrbwthblwpwpbzvjvhzsphmfhfwvsthlfnhhfcmpsnmgrvrntlzpdvqwtrghnslnfhcjwrsvrngqqtwvcsfhbjwmsnmsmgvdhnzjgljtchbtwlfppvbtdclbdjdmwzcntvgfjlcwdplnjwqnzqhnfgcnbrgftqpdmqzrrhglbzzvjcdnbtfnvmsrbjdzhbqmhnsmprgvjzzgvllhqnzgpstqzcnlgsrcwzlhwqvcjlwnnjslmdtwqcpbrntrmrmmtscjwwtzjhghtqvvpldzvhtmspzlnlfgrfhmsndbdgpgvphwwgqhrtlwztgqqsrwnrnqphqfsrtbztqbrgmfbtpjwhhrglhbzmmjptppnfdzlpbqfcbdwzdtqbrvfmtdzdjlnzvqfnzmttpqgzgmrqwmdtmdzrttffpdlgwdhnlrhnnztphvrbzcrlvcpswlngcjhdzqwwwpzdmhhwpnzwgjsdsdbdvpfsrwmwvsggpcqbchwjpgljnbtpvjzbbvgsbsbjmtwtbjtzzsfvrmfvnmcngvvdsvljvjbrlfgstjrhtjplttzhjfbmphvbqdsmwfwspqpcvmgzgjnqlphshlgdwcvtmpwcfgdcbqwpnshfgrfjvlrtqbffwwtbnwtvjlsdgwgfmhlrsmfrjzcwccdzfwwdwhwdsjbllhjsqmnqvngvdmbvbssfjtjfbtngrdwgldcrtpmvrbrmpvwwsfrlnbqsqzfnftpbhslqccnbqwgbdbfpblpmwbgjzmnptnhdjzqjhdrhqbtfhsrdqwlmwzqlsmmslgfzpvtgtsrlszvqrhrzclbqhzzwwfmhrrvsrnsjbdjsqqlsmgdmgbdtmvfjmsbwjqmqrvrhqbchpqrwvlvwpvhjlbdzfjvrwmchccrsrfvhzmpfjqwnrbvqmgwjcbndjdtfgnrzrqwgzhrdvghdrvgtplcrthgchmvwtdrchfwpdszzzhqpmrlzvfdnfnlwghmmwvsscbrdbchhgttsnbzdbqgddqfvcgvqwltnqtcwrmhtftnlwvlglsvvctccnntznsjnmmgqlzmplsdspnjtmzlbvrfzfclnhgjzmvntdwhspqwtpgndspnjqjqwrpwhjhpvjwfptpndnwvcjdwsvdtcrtwpsprgmrspgmcsdgtjbbgsgvcjhrcldlvgvqwqwthplzgwbzmszjfrlnznvgphnqzcwsztvvljlrlzrndbzccstprhntnlmshhclnrsmsvvvsbmpfdjsmspwcqtmlrrdmfzjjjhmsmdfqddzpgtbzbsnhhhpsfrdrdvpvpnjmvnhdrzrqggrpqdcmctvqfrtfmjjqjwgzzbrdfplhzjbnqlmjlcgvmsbpgdlfjmbgqtrvzzdgtlmbqthjrdtlstqtzqvfjvmmstsmtsbnjvstjjvrrjqcbjvhfpslpvjmdznrcnsvlpbpzmslqtpczmvhdwzrhwbwtfvrrmbszvrhwsjrclcscgngwvblbbrqprgshwzhlqgwmpfsmqsvpjbdccdmtnnhqfwvlgjlszmmmdmtmpzwhplzsjztrnwngbvspqqbmghwzgvfjdrblfmtwcvnczsrflmsjmrsvzldmttjwcmnvwcbjfvznhgntnqfbfchcqqshhjldgltqhdlqldlpfjnjvtbvbntzdjzstcqbzdnmsvcdgvjmmvtdfvdplqfndqqlzlspmjgdfbgsvwzqzsvvbbldltbtzwzpqrzfmfzgdbpqnwtrfcgwmlbpzrgscbjvfdwnjzjdfzltsbppnljzrgggplmttpmgwnhdlwfhwzsrcflnrqqzwsbqllwjqlrgwbhvcvqdvjvpbzgnfbbbtccvplzggplbrsbldllwmttwtvltsfljfbbprtvlfshhwdhdgvzfzjttvnphpnjnzsbvfwflfpqwnhvwjdsrtbwsjzqhgfldnssfbbzzqqrwtjvwjschmndgqzjtpsbfhwtmqbtfstrbghgtnldjqtshdnrwzvwddchhvdbsfjnqzfjdpvhvwwjspftgbtgwzdfgzzhpvjpdlrrdfnpftshthwzjzmzdghnfdqcbmjhfdgzrcgrzbrjtmhwbjhcpgjdsmnqzncdlwhqqzqblgdbbdsmrqgbdbmdczvvpnbbjdwrlmrwgnnbbzpcnsjgcmshgzwnjzwjlrdmvmhvjrzphgpczppqvwjthcdphprhhrggjdpzmgtpjjfvpczzrvsssfrrptnzlstrhmbhvzmwjnddshrrtgspbllvqlsptrtvtldsgnjjbwtfmtbjdvmgbptjlzhpttjmvpgnjphswhtdq
"""
actual_input = actual_input.split("\n")[1:-1][0]
print(actual_input)

resp = None
for i in range(14, len(actual_input)):
    if len(set(actual_input[i - 14:i])) == 14:
        resp = i
        break
print(resp)
