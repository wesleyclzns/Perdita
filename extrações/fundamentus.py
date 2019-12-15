import mechanize
from bs4 import BeautifulSoup as bs
import http.cookiejar as cookielib

cookies = cookielib.CookieJar()  # cria um repositório de cookies
browser = mechanize.Browser()    # inicia um browser
browser.set_cookiejar(cookies)   # aponta para o seu repositório de cookies

# substitua 'seu_id' por um id válido que você tenha acesso
browser.open('https://fundamentei.com/login')

browser.select_form(nr=0)      # o formulário de senha é o primeiro
browser.form['wesleycalazans14@gmail.com'] = 'seu_emaik'     # substitua 'seu_email' pelo seu e-mail
browser.form['password'] = 'senha'  # substitua 'senha' pela sua senha
browser.submit()               # submissão dos dados

pagina = browser.response().read()  # essa é a página que você queria 

# Beautiful Soup aqui
soup = bs(pagina,'html.parser')
codigo = soup.find("pre",{"id":"code"}).text

print(codigo) # o dado que você buscava


papel = ""
"http://www.fundamentus.com.br/detalhes.php?papel=ANIM3"