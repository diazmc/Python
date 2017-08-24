function parensValid(str){
    var count = 0 
    var bull = true
    for (var i = 0; i <str.length; i ++) {
        if (str[i]=="(") {
            count ++;
        }
        else if (str[i] == ")") {
            count --;
        }
        if (count == -1) {
            bull = false
            break;
        }

        if (count != 0) {
            bull=false
        }
    }
}

parensValid ()