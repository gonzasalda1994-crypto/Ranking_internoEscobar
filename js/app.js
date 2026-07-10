let jugadores = [];

async function cargarRanking(tipo = "clasico") {

    try {

        const respuesta = await fetch(`data/${tipo}.json`);

        jugadores = await respuesta.json();

        mostrarTabla(jugadores);

    } catch (error) {

        console.error(error);

    }

}

function mostrarTabla(lista) {

    const tabla = document.getElementById("tablaRanking");

    tabla.innerHTML = "";

    lista.forEach((jugador, index) => {

        // Busca automáticamente la columna del ELO
        const columnaElo = Object.keys(jugador).find(c => c.toLowerCase().includes("elo"));

        tabla.innerHTML += `
        <tr>
            <td>${index + 1}</td>
            <td>${jugador.Nombre}</td>
            <td>${jugador[columnaElo]}</td>
        </tr>
        `;

    });

}

function filtrar() {

    const texto = document
        .getElementById("buscar")
        .value
        .toLowerCase();

    const resultado = jugadores.filter(j =>
        j.Nombre.toLowerCase().includes(texto)
    );

    mostrarTabla(resultado);

}

cargarRanking();