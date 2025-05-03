//O principal objetivo deste desafio é fortalecer suas habilidades em lógica de programação. Aqui você deverá desenvolver a lógica para resolver o problema.

let amigoImput = document.getElementById("amigo");
let printarNomes = document.getElementById("listaAmigos");
let resultado = document.getElementById("resultado");
let nomesLista = [];

function adicionarAmigo(){
    let nome = amigoImput.value;
    if(nome.trim() !== '') { // trim() remove espaços em branco do início e final
        nomesLista.push(nome);
        printarNomes.innerHTML = '';
        
        
        for (let i in nomesLista){
            printarNomes.innerHTML += `<p>${nomesLista[i]}</p>`;
        }
        
        limparInput();
        resultado.innerHTML=''
    }
    else{
        alert("por favor, insira um nome válido")
    }
}

function limparInput(){
    amigoImput.value = '';
}

function getRandomInt(max) {
    return Math.floor(Math.random() * max);
  }
function sortearAmigo(){
    if (nomesLista.length !=0) {
    amigoSorteado = getRandomInt(nomesLista.length)
    resultado.innerHTML=`o amigo secreto sorteado é: ${nomesLista[amigoSorteado]}` 
    nomesLista=[]
    printarNomes.innerHTML = '';
    }
}

