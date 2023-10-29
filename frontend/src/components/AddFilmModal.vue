<template>
  <div class="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">

        <div class="modal-header">
          <h2 class="modal-title fs-5" id="staticBackdropLabel">Add Film Details Here</h2>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>

        <div class="modal-body">
          <form @submit.prevent="addFilm">
            <label for="title">Title:</label>
            <input type="text" id="title" v-model="newFilm.title" required>

            <label for="description">Description:</label>
            <textarea id="description" v-model="newFilm.description" required></textarea>

            <label for="releaseDate">Release Date:</label>
            <input type="date" id="releaseDate" v-model="newFilm.release_date" required>

            <label for="boxOffice">Box Office Amount:</label>
            <input type="number" id="boxOffice" v-model="newFilm.box_office" required>

            
          </form>
        </div>

        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          <button type="submit" class="btn btn-primary">Add Film</button>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      newFilm: {
        title: "",
        description: "",
        release_date: "",
        box_office: 0
      }
    };
  },
  methods: {
    addFilm() {
      this.$emit("add-film", this.newFilm);
    },
  }
}
</script>