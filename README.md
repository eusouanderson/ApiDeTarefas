# Documentação da API

## Descrição

Esta documentação descreve uma aplicação web que permite gerenciar tarefas. A aplicação possui três principais funcionalidades:

1. Listar tarefas existentes.
2. Adicionar novas tarefas.
3. Deletar tarefas existentes.

A aplicação utiliza a autenticação por meio de um token Bearer para acessar os endpoints.

## Tecnologias Utilizadas

A aplicação foi desenvolvida usando as seguintes tecnologias:

- **React:** Biblioteca JavaScript para construir interfaces de usuário.
- **Axios:** Cliente HTTP para fazer requisições à API.
- **Tailwind CSS:** Framework de CSS para estilização.

## Configuração

Para executar a aplicação, é necessário configurar o URL da API e o token Bearer.

- URL da API: `http://localhost:8000`
- Token Bearer: `eusouanderson:CQ5mE4c0ZtR07sBB`

Certifique-se de substituir o URL da API e o token Bearer pelos valores reais da sua aplicação.

## Componentes

A aplicação é composta por três componentes principais:

### `GetTasks`

O componente `GetTasks` é responsável por listar as tarefas existentes. Ele faz uma requisição GET para a API e exibe as tarefas retornadas.

### `DeleteTasks`

O componente `DeleteTasks` será responsável por deletar as tarefas. No entanto, ele ainda não foi implementado no código fornecido.

### `PostTasks`

O componente `PostTasks` permite adicionar novas tarefas. Ele inclui um formulário para inserir o título e a descrição da tarefa. Após a submissão do formulário, uma requisição POST é enviada à API para criar uma nova tarefa. As tarefas existentes são listadas abaixo do formulário.

## Exemplos de Uso

Aqui estão exemplos de como usar os componentes:

### Listar Tarefas

Para listar as tarefas existentes, você pode usar o componente `GetTasks`. Basta incluí-lo em seu aplicativo React para visualizar as tarefas.

```jsx
import { GetTasks } from "./GetTasks";

function App() {
  return (
    <div className="App">
      <GetTasks />
    </div>
  );
}

export default App;
