let funcao = prompt("1 para adição, 2 para subtração, 3 para multiplicação e 4 para divisão: ")
let n1 = parseFloat(prompt("Digite o 1º números: "))
let n2 = parseFloat(prompt("Digite o 2º número: "))
let prop = 0

if (funcao == 1) {
    prop = n1 + n2;
    alert("Seu resultado é " + prop);
} else if (funcao == 2) {
    prop = n1 - n2;
    alert("Seu resultado é " + prop);
} else if (funcao == 3) {
    prop = n1 * n2;
    alert("Seu resultado é " + prop);
} else if (funcao == 4) {
    prop = n1 / n2;
    alert("Seu resultado é " + prop);
} else {
    alert("Operação não encontrada!");
}
