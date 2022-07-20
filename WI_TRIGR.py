symbol_dict={'??=':'#', "??'" : "^", "??(": "[", "??)": "]", "??!": "|", "??<": "{", "??>": "}", "??-": "~", "??/":"\\"}



def translator(text):
    temp_text=[]
    translated_index=[]
    result=""
    for value in text:
        temp_text.append(value)
    
    for index, value in enumerate(temp_text):
        if index not in translated_index:
            if value == '?' and temp_text[index+1] == '?':
                temp_word=temp_text[index]+temp_text[index+1]+temp_text[index+2]
                result+=symbol_dict[temp_word]
                translated_index.append(index+1)
                translated_index.append(index+2)
                pass
            else:
                result+=value
    return result

result=translator(input())
print(result)
