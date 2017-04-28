// Funcio per centrar un element
jQuery.fn.center = function () {
    this.css("position","absolute");
    this.css("top", ( $(window).height() - this.height() ) / 2+$(window).scrollTop() + "px");
    this.css("left", ( $(window).width() - this.width() ) / 2+$(window).scrollLeft() + "px");
    return this;
}

// Funcio per assignar la poscicio horitzontal
function posHor(posActual, width1, width2, width3) {

    var posicioVert = 0

    // Si el mouse estÃ  a l'esquerra
    if ((posActual >= 0) && (posActual < width1)) {
        posicioVert = 0
    } else {

        // Si el mouse estÃ  al centre
        if ((posActual >= width1) && (posActual <= width2)) {
            posicioVert = 1
        } else {

            // Si el mouse estÃ  a la dreta
            if ((posActual > width2) && (posActual <= width3)) {
                posicioVert = 2
            }
        }
    }
    return posicioVert
}

// Funcio assignar la posicio vertical
function posVert(posActual, height1, height2, height3) {

    var posicioVert = 0

    // Si el mouse estÃ  a l'esquerra
    if ((posActual >= 0) && (posActual < height1)) {
        posicioVert = 0
    } else {

        // Si el mouse estÃ  al centre
        if ((posActual >= height1) && (posActual <= height2)) {
            posicioVert = 1
        } else {

            // Si el mouse estÃ  a la dreta
            if ((posActual > height2) && (posActual <= height3)) {
                posicioVert = 2
            }
        }
    }
    return posicioVert
}

// Quan la pagina es carrega
$(document).ready(function() {

    // Centrem la imatge
    $('#img').center();

    // Assignem les variables
    var width = $(window).width();
    var width1 = width / 3;
    var width2 = width1 * 2;
    var width3 = width;
    var height = $(window).height();
    var height1 = height / 3;
    var height2 = height1 * 2;
    var height3 = height;
    var icones = {
        '00': 'arrow-top-left',
        '01': 'arrow-left',
        '02': 'arrow-bottom-left',
        '10': 'arrow-up',
        '11': 'emoticon-happy',
        '12': 'arrow-down',
        '20': 'arrow-top-right',
        '21': 'arrow-right',
        '22': 'arrow-bottom-right'
    }


	// Classe per defecte
	$("#img").addClass('mdi mdi-48px');
	$("#img").addClass('mdi-emoticon-happy')
        
        
    // Quan es mogui el mouse
    $(document).mousemove(function(e){

        // Declarem la posicio
        var posicio = {
            horitzontal: 0,
            vertical: 0
        };

        // Assignem la posicio horitzontal
        posicio.horitzontal = posHor(e.pageX, width1, width2, width3);

        // Assignem la posicio vertical
        posicio.vertical = posVert(e.pageY, height1, height2, height3);

        // Ajuntem la posicio a un string
        posString = "" + posicio.horitzontal + posicio.vertical;

        console.log(posString);
        // Esborrem totes les classes
        $("#img").removeClass();

        // Afegim les classes corresponents
        $("#img").addClass('mdi mdi-48px');
        $("#img").addClass('mdi-' + icones[posString])
    });


});
