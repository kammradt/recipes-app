<template>
  <v-app>
    <v-flex pa-1 text-xs-center display-3 v-text="recipe.name" />
    <v-layout justify-space-around row fill-height>
      <v-flex xs12 md6 pa-1 pt-5>
        <img
          v-if="!preview"
          class="img-fluid"
          style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);"
          :src="recipe.picture"
        />
        <img
          v-else
          class="img-fluid"
          style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);"
          :src="preview"
        />
      </v-flex>

      <v-flex xs12 md6 pa-1 pt-5>
        {{ recipe }}
        <v-form @submit.prevent="submitRecipe">
          <v-text-field
            v-model="recipe.name"
            :counter="120"
            type="text"
            label="Recipe name"
            required
          />

          <v-text-field
            v-model="recipe.ingredients"
            :counter="400"
            type="text"
            label="Ingredients"
            required
          />

          <input label="Food picture" type="file" @change="onFileChange" />

          <v-select
            v-model="recipe.difficulty"
            :items="difficultyOptions"
            label="Difficulty"
            required
          />

          <label for>
            Prep time
            <small>
              (
              <input v-model="recipe.preparation_time" type="number" />
              minutes)</small
            >
          </label>
          <v-slider v-model="recipe.preparation_time" max="600" />

          <v-textarea
            v-model="recipe.preparation_guide"
            label="Preparation guide"
            hint="Describe how to prepare your recipe here!"
            required
          />

          <v-btn type="submit">Save</v-btn>
        </v-form>
      </v-flex>
    </v-layout>
  </v-app>
</template>

<script>
export default {
  head() {
    return {
      title: 'Add Recipe'
    }
  },
  data() {
    return {
      recipe: {
        name: ' ',
        picture: '',
        ingredients: '',
        difficulty: '',
        preparation_time: 5,
        preparation_guide: ''
      },
      preview: '',
      difficultyOptions: ['Easy', 'Medium', 'Hard']
    }
  },
  methods: {
    onFileChange(e) {
      const files = e.target.files || e.dataTransfer.files
      if (!files.length) {
        return
      }
      this.recipe.picture = files[0]
      this.createImage(files[0])
    },
    createImage(file) {
      // let image = new Image();
      const reader = new FileReader()
      const vm = this
      reader.onload = e => {
        vm.preview = e.target.result
      }
      reader.readAsDataURL(file)
    },
    async submitRecipe() {
      const config = {
        headers: { 'content-type': 'multipart/form-data' }
      }
      const formData = new FormData()
      for (const data in this.recipe) {
        formData.append(data, this.recipe[data])
      }
      try {
        // eslint-disable-next-line no-unused-vars
        const response = await this.$axios.$post('/recipes/', formData, config)
        this.$router.push('/recipes/')
      } catch (e) {
        // eslint-disable-next-line no-console
        console.log(e)
      }
    }
  }
}
</script>
