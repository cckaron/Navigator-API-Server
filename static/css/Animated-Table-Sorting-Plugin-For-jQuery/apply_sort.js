function addnewdata(){
    var x = Math.floor((Math.random() * 3));
    var distance = (Math.random() * 10 + 1).toFixed(1);
    var time = Math.round(Math.sqrt(distance)*2)
    if(x==0){
        var dick = "<tr class='block safe'><td class='text safe'>0</td><td><h4>"+time+"分鐘</h4></td><td>"+distance+"公里</td></tr>";
    } else if(x==1){
        var dick = "<tr class='block warning'><td class='text warning'>1</td><td><h4>"+time+"分鐘</h4></td><td>"+distance+"公里</td></tr>";
    } else if(x==2){
        var dick = "<tr class='block danger'><td class='text danger'>2</td><td><h4>"+time+"分鐘</h4></td><td>"+distance+"公里</td></tr>";
    }
    $("table").append(dick);
}
var raw_table;

$(document).ready(function() {
    var i;
    for (i = 0; i < 15; i++) {
        addnewdata();
    }
    raw_table = $("table");
    $("table").tableSort( {
    animation :'slide',
    speed:600
    } );
    
})

function sort_by_category(){
    setTimeout(function(){
        $("table tr th.col-0").trigger('click');
    },5000);
}

function mainloop(){
    setInterval(function(){
        /*var x = Math.floor((Math.random() * 3));
        var distance = (Math.random() * 10).toFixed(1);
        var time = Math.round(Math.sqrt(distance)*2)
        if(x==0){
            var dick = "<tr class='block safe'><td class='text safe'>0</td><td><h4>"+time+"分鐘</h4></td><td>"+distance+"公里</td></tr>";
        } else if(x==1){
            var dick = "<tr class='block warning'><td class='text warning'>1</td><td><h4>"+time+"分鐘</h4></td><td>"+distance+"公里</td></tr>";
        } else if(x==2){
            var dick = "<tr class='block danger'><td class='text danger'>2</td><td><h4>"+time+"分鐘</h4></td><td>"+distance+"公里</td></tr>";
        }
        raw_table.append(dick);
        raw_table.tableSort( {
            animation :'slide',
            speed:600
            } );
        setTimeout(function(){
            $("table tr th.col-0").trigger('click');
        },5000)*/
        $("table tr th.col-0").trigger('click');
    },5000);
}

mainloop();
