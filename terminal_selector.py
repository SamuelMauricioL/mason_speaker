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


questions = [
    {
        'type': 'list',
        'message': 'Select brick',
        'name': 'brick',
        'choices': [
            Separator('= The Bricks ='),
            {
                'name': 'hello'
            },
            {
                'name': 'presentation_layer'
            }
        ],
        'validate': lambda answer: 'You must choose at least one topping.'
        if len(answer) == 0 else True
    }
]

answers = prompt(questions, style=style)
print(answers)
