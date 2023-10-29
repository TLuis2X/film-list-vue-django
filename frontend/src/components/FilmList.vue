<template>
  <div>
    
    <button @click="showModal = true" type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#staticBackdrop">Add Film</button>
    <AddFilmModal v-if="showModal" @add-film="onAddFilm" />

    <div v-for="(film, index) in films" :key="index">
      <Film :film="film" :delete-film="deleteFilm" />
    </div>

  </div>
</template>

<script>
import AddFilmModal from './AddFilmModal.vue';
import Film from './Film.vue';

export default {
  components: {
    Film,
    AddFilmModal,
  },
  data() {
    return {
      films: null,
      showModal: false,
    }
  },
  methods: {
    // Fetches all films using fetch API (GET)
    fetchFilms() {
      fetch("http://localhost:8000/api/films/")
      .then(response => {
        return response.json()
      })
      .then(data => {
        this.films = data.films;
      });
    },
    // Adds a film to the database (POST)
    async onAddFilm(newFilm) {
      console.log("New Film Data:", newFilm);

      let response = await fetch('http://localhost:8000/api/films/', {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(newFilm),
      });
      console.log(response);

      if (response.ok) {
        const data = await response.json();

        this.films.push(data);

        this.showModal = false;

        this.fetchFilms();

        console.log("Response Data:", data);
      }
      else {
        throw new Error('Error creating film!!!!');
      }
    },
    // Deletes the selected film from database (DELETE)
    async deleteFilm(filmId) {
      let response = await fetch(`http://localhost:8000/api/film/${filmId}`, {
        method: "DELETE",
      });

      if (response.ok) {
        this.films = this.films.filter(f => f.id != filmId);
        console.log(response);
      }
      else {
        alert("Deleting film failed");
        console.log(response);
      }
    },
  },
  created() {
    this.fetchFilms()
  }
}
</script>
