#  Pytest Fixtures - Live de Python #168 
[Link da live no youtube](https://youtu.be/sidi9Z_IkLU)

A ideia da fixture basicamente é evitar a repetição de código em testes

```python
"""
Testes de 4 fases, Mezaros:
- setUp -> Monta o contexto que precisamos
- exercise -> Executa a ação, chama a função etc...
- assert -> Verifica o resultado
- tearDown -> Desmonta o contexto utilizado
"""
```

##### DICA 01 - De acordo com o TDD do Kent Beck o assest deve ser escrito primeiro
```python
# tests/test_do_quadro.py (antes de add a fixture)
assert len(quadro.colunas) == 1
```

Depois o teste em si
```python
# tests/test_do_quadro.py (antes de add a fixture)
def test_alguma_coisa():
    quadro = Quadro()
    quadro.inserir_coluna(Coluna(nome="A fazer"))
    assert len(quadro.colunas) == 1
```

E por fim, o nome do teste
```python
# tests/test_do_quadro.py (antes de add a fixture)
def test_quando_inserir_uma_coluna_deve_existir_uma_coluna():
    quadro = Quadro()
    quadro.inserir_coluna(Coluna(nome="A fazer"))
    assert len(quadro.colunas) == 1
```

É possível de uma fixture chamar outra fixture
```python
# tests/test_do_quadro.py
@fixture
def quadro():
    return Quadro()


@fixture
def quadro_com_coluna(quadro):
    quadro.inserir_coluna(Coluna("A"))
    return quadro
```

### Faker e Factory boy
Faker é um dublê de teste que cria objetos "de mentira" para simplificar a população de testes:
```python
from faker import Faker

fake = Faker()

@fixture
def cartao():
  return Cartao(nome=fake.pystr())
```

O factory boy é uma forma de usar o faker para gerar objetos com dados "fakes"
```python
import factory

class CartaoFactory(factory.Factory):
  class Meta:
    model = Tarefa
  
  nome = factory.Faker('pystr', max_chars=10)

@fixture
def cartao():
  return CartaoFactory.build_batch(10)
```

Existe uma forma de gerar fixtures dinâmicas passando parâmetros para elas:
```python
# tests/conftest.py
@mark.parametrize("quadro_parametrizado", [[1]], indirect=True)  # xpto
def test_passando_parametros_para_fixture(quadro_parametrizado):
    ...
```
##### Por usar o indirect ele envia o parametro passado para a fixture "quadro_parametrizado"

## Lives citadas:
- [ ] [Live de Python #76 - Dublês de teste](https://youtu.be/mOrsJwY2038)
- [ ] [Live de Python #80 - Melhorando testes de unidade com Faker, Factory boy e Hypothesis](https://youtu.be/HuZ2Keoc9Hs)
- [ ] [ Live de Python #150 - Dataclasses e obsessão por primitivos ](https://youtu.be/NtZY3AmsBSk)
- [ ] [Live de Python #151 - Desvendando o yield e as funções geradoras](https://youtu.be/ZjwZ9nfhsk4)
- [x] [Live de Python #167 - Uma visão geral sobre pytest](../live_167/README.md)