<template>
  <div>

    <div class="container" style="margin-bottom: 1rem">
      <div class="d-grid col-8 mx-auto">
        <button type="button" class="btn btn-outline-dark" data-bs-toggle="modal" data-bs-target="#staticBackdrop">
          Add Film
        </button>
      </div>
    </div>

    <div class="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">

          <div class="modal-header">
            <h1 class="modal-title fs-5" id="staticBackdropLabel">Add Film Details Here</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>

          <div class="modal-body">
            <form @submit.prevent="addFilm">
              <div class="mb-3">
                <label for="title" class="form-label">Title:</label>
                <input type="text" id="title" class="form-control" v-model="newFilm.title" required>
              </div>

              <div class="mb-3">
                <label for="description" class="form-label">Description:</label>
                <textarea class="form-control" id="description" rows="3" v-model="newFilm.description" required></textarea>
              </div>

              <div class="mb-3">              
                <label for="releaseDate" class="form-label">Release Date:</label>
                <input type="date" id="releaseDate" class="form-control" v-model="newFilm.release_date" required>
              </div>

              <div class="mb-3">
                <label for="boxOffice" class="form-label">Box Office Amount:</label>
                <input type="number" id="boxOffice" class="form-control" v-model="newFilm.box_office" required>
              </div>
              
            </form>
          </div>

          <div class="modal-footer">
            <!-- <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button> -->
            <button type="button" class="btn btn-primary" data-bs-dismiss="modal" @click="addFilm">Add Film</button>
          </div>

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