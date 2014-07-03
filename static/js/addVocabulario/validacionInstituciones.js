/**
 * Created by noescobar on 27/06/14.
 */



/*
    @name           : AplicacionVocabulario
    @author         : NelsonEonltd
    @version        : 0.1
    @description    : Esta es una clase que permite crear dentro del documento html y/o navegador todos los elementos necesario hasta la version
                      actual para cumplir con las funciones de la aplicacion de etiquetado  y agregacion de vocabulario a los juego y/o usuarios
                      a traves de la pertenencia de institucion, grupos, usuarios, juegos, etiquetas.
 */




var AplicacionVocabulario = function(mainContainer){
    this.instituciones =[];
    this.MenuOpciones = [];
    this.contenedorIntituciones = document.createElement('div');
    this.contenedorIntituciones.className = 'ContenedorLista';
    this.contenedorGrupos = document.createElement('div');
    this.contenedorGrupos.className = 'ContenedorLista';
    this.contenedorJuegos = document.createElement('div');
    this.contenedorJuegos.className = 'ContenedorLista';
    this.contenedorUsuarios = document.createElement('div');
    this.contenedorUsuarios.className = 'ContenedorLista';
    this.contenedorEtiquetas = document.createElement('div');
    this.contenedorEtiquetas.className = 'ContenedorLista';
    this.institucionSeleccionada = null;
    this.grupoSeleccionado = null;
    this.usuarioSeleccionado = null;
    this.juegoSeleccionado = null;
    this.EtiquetaSeleccionada = null;
    this.container = document.createElement('div');
    this.container.id = 'contenedorAplicacion';
    this.mainContainer = mainContainer;
    this.peticiones = new Peticiones();
};


AplicacionVocabulario.prototype.generarInstituciones = function(){
    var insEncontradas = this.peticiones.buscarInstituciones();
    var posicion;
    for(posicion in insEncontradas){
        this.instituciones.push(new Institucion(insEncontradas[posicion],this.contenedorIntituciones,this.peticiones,this))
    }
    insEncontradas = null;
};





AplicacionVocabulario.prototype.crearAplicacion = function(){
    this.mainContainer.appendChild(this.container);
    this.container.appendChild(this.contenedorIntituciones);
};



AplicacionVocabulario.prototype.recargarDesde = function(child){
    var posicion;
    var childFueEncontrado = false;
    var childEnc;
    var childsToRemove = []
    if(child.parentNode != null) {
        for (posicion = 0; posicion < this.container.childNodes.length ; posicion++) {
            childEnc = this.container.childNodes[posicion];
            if (childFueEncontrado) {
                childsToRemove.push(childEnc);
            }
            if (childEnc == child) {
                childFueEncontrado = true;
            }
        }
        for (posicion = 0; posicion < childsToRemove.length; posicion++) {
            this.container.removeChild(childsToRemove[posicion]);
        }
    }
};




/*
    @name           : Peticiones
    @author         : NelsonEonltd
    @version        : 0.1
    @description    : Esta es una clase que busca cumplir con las funciones de peticiones al servidor en la aplicacion
 */



var Peticiones = function(){

};


/*
    @name           : burcarInstituciones
    @author         : NelsonEonltd
    @version        : 0.1
    @description    : este metodo es utilizado para manejar la generacion de las instituciones a traves de peticion ajax al servidor, la validacion del usuario
                      a cargo de la institucion esta trabajada en el servidor, por lo tanto no se podra acceder a una institucion si no se esta logueado

 */

Peticiones.prototype.buscarInstituciones = function() {
    var instituciones = null;
    $.ajax(
        {
            beforeSend: function(){
                            console.log('buscando Instituciones...');
                        },
            url: "/vocabulario/buscarInstituciones_ajax/",
            method: 'GET',
            type: 'JSON',
            async: false,
            success: function(result){
                        instituciones = result;
                        console.log('conseguido');
                    },
            failure: function () {
                        console.log('un Error a Ocurrido');
                    }
        }
    );

    return instituciones;
};


/*
    @name           : burcarGrupos
    @author         : NelsonEonltd
    @version        : 0.1
    @description    : este metodo cumple la funcion de enviar un peticion al servidor para buscar los grupos a cargo de una
                      una institucion por eso es necesario que se le pase como parametro la institucion deseada
 */







Peticiones.prototype.buscarGrupos = function(institucion) {
    var grupos = null;
    //serializado = JSON.stringify(institucion.elementoJson);
    $.ajax(
        {
            beforeSend: function(){
                            console.log('buscando grupos...');
                        },
            url: "/vocabulario/buscarGrupos_ajax/",
            data: {'institucion' : institucion.elementoJson.pk},
            dataType: 'json',
            method: 'GET',
            type: 'JSON',
            async: false,
            success: function(result){
                        if ( typeof  result == "string") {
                            console.log(result);
                            grupos = []
                        }
                        else{
                            grupos = result;
                            console.log('conseguido');
                        }
                    },
            failure: function () {
                        console.log('un Error a Ocurrido');
                    }
        }
    );

    return grupos;
};








/*
    @name           : burcarUsuarios
    @author         : NelsonEonltd
    @version        : 0.1
    @description    : este metodo cumple la funcion de enviar un peticion al servidor para buscar los usuario a cargo de una
                      un grupo por eso es necesario que se le pase como parametro el grupo deseado.
 */





Peticiones.prototype.buscarUsuarios = function(grupo) {
    var usuarios = null;
    //serializado = JSON.stringify(institucion.elementoJson);
    $.ajax(
        {
            beforeSend: function(){
                            console.log('buscando Usuarios...');
                        },
            url: "/vocabulario/buscarUsuarios_ajax/",
            data: {'grupo' : grupo.elementoJson.pk},
            dataType: 'json',
            method: 'GET',
            type: 'JSON',
            async: false,
            success: function(result){
                        if ( typeof  result == "string") {
                            console.log(result);
                            usuarios = []
                        }
                        else{
                            usuarios = result;
                            console.log('conseguido');
                        }
                    },
            failure: function () {
                        console.log('un Error a Ocurrido');
                    }
        }
    );

    return usuarios;
};




/*
    @name           : burcarJuegos
    @author         : NelsonEonltd
    @version        : 0.1
    @description    : este metodo cumple la funcion de enviar un peticion al servidor para buscar los usuario a cargo de una
                      un grupo por eso es necesario que se le pase como parametro el grupo deseado.
 */





Peticiones.prototype.buscarJuegos = function(grupo) {
    var juegos = null;
    //serializado = JSON.stringify(institucion.elementoJson);
    $.ajax(
        {
            beforeSend: function(){
                            console.log('buscando Juegos...');
                        },
            url: "/vocabulario/buscarJuegos_ajax/",
            data: {'grupo' : grupo.elementoJson.pk, 'institucion': grupo.institucion.elementoJson.pk},
            dataType: 'json',
            method: 'GET',
            type: 'JSON',
            async: false,
            success: function(result){
                        if ( typeof  result == "string") {
                            console.log(result);
                            juegos = []
                        }
                        else{
                            juegos = result;
                            console.log('conseguido');
                        }
                    },
            failure: function () {
                        console.log('un Error a Ocurrido');
                    }
        }
    );

    return juegos;
};




/*
    @name           : burcarEtiquetas
    @author         : NelsonEonltd
    @version        : 0.1
    @description    : este metodo cumple la funcion de enviar un peticion al servidor para buscar las etiquetas con valores
                      de pertenencia correspondientes a un juego o incluso a un usuario.
 */





Peticiones.prototype.buscarEtiquetasInstitucion = function(institucion) {
    var etiquetas;
    var tipo = 'juego';
    //serializado = JSON.stringify(institucion.elementoJson);
    $.ajax(
        {
            beforeSend: function(){
                            console.log('buscando Juegos...');
                        },
            url: "/vocabulario/buscarEtiquetas_ajax/",
            data: {'institucion' : institucion.elementoJson.pk},
            dataType: 'json',
            method: 'GET',
            type: 'JSON',
            async: false,
            success: function(result){
                        if ( typeof  result == "string") {
                            console.log(result);
                            etiquetas = []
                        }
                        else{
                            etiquetas = result;
                            console.log('conseguido');
                        }
                    },
            failure: function () {
                        console.log('un Error a Ocurrido');
                    }
        }
    );

    return etiquetas;
};








/*
    @name           : Institucion
    @author         : NelsonEonltd
    @version        : 0.1
    @description    : esta clase puede verse como un modelo de las intituciones que esta encargada de representar a las instituciones traidas por un peticion
                      se creara un contenedor que representa a la institucion en el documento html y permite referenciarlo dentro de un  contenedorPrincipal
                      por defecto se genera el elemento dentro del document.
 */




var Institucion = function(objetoJson, mainContainer, peticiones, aplicacion){
    this.elementoJson = objetoJson;
    this.habilitado = objetoJson.fields['habilitado'];
    this.nombre = objetoJson.fields['nombre'];
    this.container = document.createElement('div');
    this.mainContainer = mainContainer;
    this.generarELemento();
    this.peticiones = peticiones;//new Peticiones();
    this.grupos = null;
    var self = this;
    this.aplicacion = aplicacion;
    this.container.onclick = function () {
                                 self.ponerListaGrupos();
                             };
};



/*
    @name           : generarElemento
    @author         : NelsonEonltd
    @version        : 0.1
    @description    : Este metodo permite que el elemento institucion sea generado dentro del contenedor correspondiente en la pagina web, ademas de cumplir con la modificacion
                      de este dependiendo si esta o no esta habilidato.
 */




Institucion.prototype.generarELemento = function(){
    this.mainContainer.appendChild(this.container);
    this.container.innerHTML = "<p>"+this.nombre+"</p>";
    this.container.className = 'Elemento';
    if( this.habilitado ){
        this.container.style.backgroundColor = "green";
    }
};



Institucion.prototype.ponerListaGrupos = function () {
    var posicion;
    if(this.aplicacion.institucionSeleccionada != this){
        this.aplicacion.recargarDesde(this.mainContainer);
    }
    if (this.grupos == null) {
        this.grupos = [];
        gruposJson = this.peticiones.buscarGrupos(this);
        if(this.aplicacion.contenedorGrupos.hasChildNodes()){
            this.aplicacion.contenedorGrupos.innerHTML = ""
        }
        if(this.aplicacion.contenedorGrupos.parentNode == null){
            if (this.aplicacion.contenedorIntituciones.nextSibling) {
              this.aplicacion.contenedorIntituciones.parentNode.insertBefore(this.aplicacion.contenedorGrupos,this.contenedorIntituciones.nextSibling);
            }
            else {
                this.aplicacion.contenedorIntituciones.parentNode.appendChild(this.aplicacion.contenedorGrupos);
            }
        }
        for(posicion in gruposJson){
            this.grupos.push(new Grupo(gruposJson[posicion],this.aplicacion.contenedorGrupos,this))
        }
        this.aplicacion.institucionSeleccionada = this;

    }else{
        if(this.aplicacion.institucionSeleccionada == this && this.mainContainer.parentNode != null){
            alert('los grupos que pueden ser manejados por la institucion ' + this.nombre + ' ya han sido generado');
        }
        else {
            if(this.aplicacion.contenedorGrupos.hasChildNodes()){
                this.aplicacion.contenedorGrupos.innerHTML = "";
            }
            if(this.aplicacion.contenedorGrupos.parentNode == null){
                if (this.aplicacion.contenedorIntituciones.nextSibling) {
                  this.aplicacion.contenedorIntituciones.parentNode.insertBefore(this.aplicacion.contenedorGrupos,this.contenedorIntituciones.nextSibling);
                }
                else {
                    this.aplicacion.contenedorIntituciones.parentNode.appendChild(this.aplicacion.contenedorGrupos);
                }
            }
            for(posicion in this.grupos){
                this.aplicacion.contenedorGrupos.appendChild(this.grupos[posicion].container);
            }
            this.aplicacion.institucionSeleccionada = this;
        }
    }
};




var Grupo = function(objetoJson, mainContainer,institucion){
    this.elementoJson = objetoJson;
    this.habilitado = objetoJson.fields['habilitado'];
    this.nombre = objetoJson.fields['nombre'];
    this.container = document.createElement('div');
    this.mainContainer = mainContainer;
    this.generarELemento();
    this.peticiones = institucion.peticiones; // new Peticiones();
    this.juegos = null;
    var self = this;
    this.institucion = institucion;
    this.aplicacion = institucion.aplicacion;
    this.container.onclick = function() {
         if(!self.estaSobreElmenu()) {
             self.ponerListaJuegos();
         };
    };
    this.container.onmouseover = function () {
        self.container.appendChild(self.contenedorMenu);
    };
    this.container.onmouseout = function () {
        if(!self.estaSobreElmenu()) {
            self.container.removeChild(self.contenedorMenu)
        }
    }
    this.contenedorMenu = null;
    this.crearMenu();
};



Grupo.prototype.crearMenu = function(){
    var contenedorMenu =  document.createElement('div');
    contenedorMenu.className = 'menuDeGrupo';
    var posicion = $(this.container).position();
    contenedorMenu.style.position = 'absolute';
    $(contenedorMenu).css('left',posicion.left + this.container.offsetWidth -5);
    $(contenedorMenu).css('top',posicion.top + this.container.offsetHeight*(0.25));
    var opcionUsuarios = document.createElement('div');
    opcionUsuarios.innerHTML = '<p>Usuarios</p>';
    var self  = this;
    opcionUsuarios.onclick = function(){
        self.ponerListaUsuario();
    };
    var opcionJuegos = document.createElement('div');
    opcionJuegos.innerHTML = '<p>Juegos</p>';
    opcionJuegos.onclick = function(){
        self.ponerListaJuegos();
    };
    contenedorMenu.appendChild(opcionUsuarios);
    contenedorMenu.appendChild(document.createElement('hr'));
    contenedorMenu.appendChild(opcionJuegos);
    //contenedorMenu.innerHTML = opcionUsuarios.innerHTML+'<hr/>'+opcionJuegos.innerHTML
    this.contenedorMenu = contenedorMenu;

}

Grupo.prototype.estaSobreElmenu= function(){
    var mouseX= window.event.clientX;
    var mouseY= window.event.clientY;
    var posicionContenedor = $(this.contenedorMenu).position();
    if((mouseX >= posicionContenedor.left-5 && mouseX <= (posicionContenedor.left+this.contenedorMenu.offsetWidth) ) && (mouseY >= posicionContenedor.top && mouseY <= (posicionContenedor.top+this.contenedorMenu.offsetHeight ))){
        return true;
    }
    else{
        return false;
    }
};


/*
*
* !!!!!!!!!!!!!!!!!!!!!!!!!!!!aun sin adaptar a la clase Grupo
*
*
* */


Grupo.prototype.generarELemento = function(){
    this.mainContainer.appendChild(this.container);
    this.container.innerHTML = "<p>"+this.nombre+"</p>";
    this.container.className = 'Elemento';
    if( this.habilitado ){
        this.container.style.backgroundColor = "green"
    }
}


Grupo.prototype.ponerListaUsuario = function(){
    usuarioJson = this.peticiones.buscarUsuarios(this);
    console.log(usuarioJson);

};


Grupo.prototype.ponerListaJuegos = function(){
    var posicion;
    if(this.aplicacion.grupoSeleccionado != this){
        this.aplicacion.recargarDesde(this.mainContainer)
    }
    if (this.juegos == null) {
        this.juegos = [];
        juegosJson = this.peticiones.buscarJuegos(this);
        if(this.aplicacion.contenedorJuegos.hasChildNodes()){
            this.aplicacion.contenedorJuegos.innerHTML = ""
        }
        if(this.aplicacion.contenedorJuegos.parentNode == null){
            if (this.aplicacion.contenedorGrupos.nextSibling) {
              this.aplicacion.contenedorGrupos.parentNode.insertBefore(this.aplicacion.contenedorJuegos,this.contenedorGrupos.nextSibling);
            }
            else{
                if(this.aplicacion.contenedorUsuarios.parentNode != null) {
                    this.aplicacion.contenedorUsuarios.parentNode.removeChild(this.aplicacion.contenedorUsuarios)
                }
                this.aplicacion.contenedorIntituciones.parentNode.appendChild(this.aplicacion.contenedorJuegos);
            }
        }
        for(posicion in juegosJson){
            this.juegos.push(new Juego(juegosJson[posicion],this.aplicacion.contenedorJuegos,this))
        }
        this.aplicacion.grupoSeleccionado = this

    }else{
        if(this.aplicacion.grupoSeleccionado == this && this.aplicacion.contenedorJuegos.parentNode != null){
            alert('los juegos que pueden ser agregados por el grupo ' + this.nombre + ' ya han sido generados');
        }
        else {
            if(this.aplicacion.contenedorJuegos.hasChildNodes()){
                this.aplicacion.contenedorJuegos.innerHTML = ""
            }
            if(this.aplicacion.contenedorJuegos.parentNode == null){
                if (this.aplicacion.contenedorGrupos.nextSibling) {
                  this.aplicacion.contenedorGrupos.parentNode.insertBefore(this.aplicacion.contenedorJuegos,this.contenedorGrupos.nextSibling);
                }
                else{
                    if(this.aplicacion.contenedorUsuarios.parentNode != null) {
                        this.aplicacion.contenedorUsuarios.parentNode.removeChild(this.aplicacion.contenedorUsuarios)
                    }
                    this.aplicacion.contenedorIntituciones.parentNode.appendChild(this.aplicacion.contenedorJuegos);
                }
            }
            for(posicion in this.juegos){
                this.aplicacion.contenedorJuegos.appendChild(this.juegos[posicion].container)
            }
            this.aplicacion.grupoSeleccionado = this
        }
    }
};


/*
*
*
*
*
* */




var Juego = function(objetoJson, mainContainer,grupo){
    this.elementoJson = objetoJson;
    this.habilitado = true;
    this.nombre = objetoJson.fields['nombre'];
    this.container = document.createElement('div');
    this.mainContainer = mainContainer;
    this.generarELemento();
    this.peticiones = grupo.peticiones; // new Peticiones();
    this.etiquetas = null;
    var self = this;
    this.grupo = grupo;
    this.aplicacion = grupo.aplicacion
    this.container.onclick = function() {
        self.ponerListaEtiquetas()
    };
    this.checkbox = document.createElement('input');
    this.checkbox.type = 'checkbox';
    this.checkbox.checked = this.habilitado;
    this.checkbox.className = 'checkbox';
    this.container.appendChild(this.checkbox);
};



Juego.prototype.generarELemento = function(){
    this.mainContainer.appendChild(this.container);
    this.container.innerHTML = "<p>"+this.nombre+"</p>";
    this.container.className = 'Elemento';
    this.container.style.backgroundColor = "white";
}



Juego.prototype.ponerListaEtiquetas = function(){
    var posicion;
    if (this.etiquetas == null) {
        this.etiquetas = [];
        etiquetasJson = this.peticiones.buscarEtiquetasInstitucion(this.grupo.institucion);
        if(this.aplicacion.contenedorEtiquetas.hasChildNodes()){
            this.aplicacion.contenedorEtiquetas.innerHTML = ""
        }
        if(this.aplicacion.contenedorEtiquetas.parentNode == null){
            if (this.aplicacion.contenedorJuegos.nextSibling) {
              this.aplicacion.contenedorJuegos.parentNode.insertBefore(this.aplicacion.contenedorEtiquetas,this.contenedorJuegos.nextSibling);
            }
            else{
                this.aplicacion.contenedorIntituciones.parentNode.appendChild(this.aplicacion.contenedorEtiquetas);
            }
        }
        for(posicion in etiquetasJson){
            this.etiquetas.push(new Etiqueta(etiquetasJson[posicion],this.aplicacion.contenedorEtiquetas,this))
        }
        this.aplicacion.juegoSeleccionado = this

    }else{
        if(this.aplicacion.juegoSeleccionado == this && this.aplicacion.contenedorEtiquetas.parentNode != null){
            alert('las etiquetas que pueden ser agregados por el grupo ' + this.nombre + ' ya han sido generadas');
        }
        else {
            if(this.aplicacion.contenedorEtiquetas.hasChildNodes()){
                this.aplicacion.contenedorEtiquetas.innerHTML = "";
            }
            if(this.aplicacion.contenedorEtiquetas.parentNode == null){
                if (this.aplicacion.contenedorJuegos.nextSibling) {
                  this.aplicacion.contenedorJuegos.parentNode.insertBefore(this.aplicacion.contenedorEtiquetas,this.contenedorJuegos.nextSibling);
                }
                else{
                    this.aplicacion.contenedorIntituciones.parentNode.appendChild(this.aplicacion.contenedorEtiquetas);
                }
            }
            for(posicion in this.etiquetas){
                this.aplicacion.contenedorEtiquetas.appendChild(this.etiquetas[posicion].container);
            }
            this.aplicacion.juegoSeleccionado = this;
        }
    }
}



var Etiqueta = function(objetoJson, mainContainer,asignado){
    this.elementoJson = objetoJson;
    this.habilitado = true;
    this.nombre = objetoJson.fields['nombre'];
    this.container = document.createElement('div');
    this.mainContainer = mainContainer;
    this.generarELemento();
    this.peticiones = asignado.peticiones; // new Peticiones();
    this.etiquetas = null;
    var self = this;
    this.asignado = asignado;
    this.container.onclick = function() {
        //alert(self.nombre)
    };
    this.checkbox = document.createElement('input');
    this.checkbox.type = 'checkbox';
    this.checkbox.checked = this.habilitado;
    this.checkbox.className = 'checkbox';
    $(this.checkbox).css({
        'float' : 'right',
        'margin-top' : '-50px'
    })
    this.container.appendChild(this.checkbox);
}



Etiqueta.prototype.generarELemento = function(){
    this.mainContainer.appendChild(this.container);
    this.container.innerHTML = "<p>"+this.nombre+"</p>"+"<p style='color-text: chartreuse;' >"+this.elementoJson.fields['pertenecen']+"</p>";
    this.container.className = 'Elemento';
    this.container.style.backgroundColor = "white";
}



var nuevaAplicacion = new AplicacionVocabulario(document.getElementsByTagName('body')[0]);


nuevaAplicacion.crearAplicacion();

nuevaAplicacion.generarInstituciones();
