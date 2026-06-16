let dict_estoque = {
    'valor': [35, 25, 33, 40]
};
despesa = 0;
for(i=0;i<dict_estoque['valor'].length;i++){
    despesa += dict_estoque['valor'][i]
};
console.log(despesa)