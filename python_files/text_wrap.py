import textwrap

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width)
  
    dedented_text = textwrap.dedent(text=string)
    original = wrapper.fill(text=dedented_text)
    return original

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)