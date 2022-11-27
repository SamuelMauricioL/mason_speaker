from PyInquirer import style_from_dict, Token, prompt, Separator


style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})


def selector_cli(list, parameter_name):
    options = []
    for item in list:
        options.append({'name': item})
    questions = [
        {
            'type': 'list',
            'message': 'Select brick',
            'name': parameter_name,
            'choices': options,
            'validate': lambda answer: 'You must choose at least one topping.'
            if len(answer) == 0 else True
        }
    ]

    return prompt(questions, style=style)
