function Team(name,city,color){
    this.name = name;
    this.city = city;
    this.color = color;
    this.players = [];
}

function Player(p_name,j_number,){
    this.p_name = p_name;
    this.j_number = j_number;
}

var seahawks = new Team("seahawks", "seattle", "blue");

var russ = new Player("r_wilson", 3)
console.log(seahawks)
