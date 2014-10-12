var pageExecute = {

    fileContents:"Null",
    pagePrefix:"Null",
    slides:"Null",

    init: function () {
        $.ajax({
            url: "C:\Users\Cory\Documents\PHP\read\file.txt",
            async: false,
            success: function (data){
                pageExecute.fileContents = data;
            }
        });
    }
};