<template>
  <v-app>
    <v-toolbar dark class="primary" flat>
      <v-toolbar-title>Receitinhas top</v-toolbar-title>
      <v-spacer />
      <nuxt-link to="/recipes/add">
        <v-btn outline>Add</v-btn>
      </nuxt-link>
    </v-toolbar>
    <br />
    <v-layout align-start justify-start row wrap>
      <template v-for="recipe in recipes">
        <RecipeCard :key="recipe.id" :on-delete="deleteRecipe" :recipe="recipe">
        </RecipeCard>
      </template>
    </v-layout>
  </v-app>
</template>

<script>
import RecipeCard from '~/components/RecipeCard.vue'

const sampleData = [
  {
    id: 1,
    name: 'Jollof Rice',
    picture: '/images/food-1.jpeg',
    ingredients: 'Beef, Tomato, Spinach',
    difficulty: 'easy',
    prep_time: 15,
    prep_guide:
      'Lorem ipsum dolor sit amet consectetur adipisicing elit. Omnis, porro. Dignissimos ducimus ratione totam fugit officiis blanditiis exercitationem, nisi vero architecto quibusdam impedit, earum '
  },
  {
    id: 2,
    name: 'Macaroni',
    picture: '/images/food-2.jpeg',
    ingredients: 'Beef, Tomato, Spinach',
    difficulty: 'easy',
    prep_time: 15,
    prep_guide:
      'Lorem ipsum dolor sit amet consectetur adipisicing elit. Omnis, porro. Dignissimos ducimus ratione totam fugit officiis blanditiis exercitationem, nisi vero architecto quibusdam impedit, earum '
  },
  {
    id: 3,
    name: 'Fried Rice',
    picture: '/images/banner.jpg',
    ingredients: 'Beef, Tomato, Spinach',
    difficulty: 'easy',
    prep_time: 15,
    prep_guide:
      'Lorem ipsum dolor sit amet consectetur adipisicing elit. Omnis, porro. Dignissimos ducimus ratione totam fugit officiis blanditiis exercitationem, nisi vero architecto quibusdam impedit, earum '
  },
  {
    id: 4,
    name: 'Fried Rice',
    picture: '/images/banner.jpg',
    ingredients: 'Beef, Tomato, Spinach',
    difficulty: 'easy',
    prep_time: 15,
    prep_guide:
      'Lorem ipsum dolor sit amet consectetur adipisicing elit. Omnis, porro. Dignissimos ducimus ratione totam fugit officiis blanditiis exercitationem, nisi vero architecto quibusdam impedit, earum '
  },
  {
    id: 5,
    name: 'Fried Rice',
    picture: '/images/banner.jpg',
    ingredients: 'Beef, Tomato, Spinach',
    difficulty: 'easy',
    prep_time: 15,
    prep_guide:
      'Lorem ipsum dolor sit amet consectetur adipisicing elit. Omnis, porro. Dignissimos ducimus ratione totam fugit officiis blanditiis exercitationem, nisi vero architecto quibusdam impedit, earum '
  },
  {
    id: 6,
    name: 'Fried Rice',
    picture: '/images/banner.jpg',
    ingredients: 'Beef, Tomato, Spinach',
    difficulty: 'easy',
    prep_time: 15,
    prep_guide:
      'Lorem ipsum dolor sit amet consectetur adipisicing elit. Omnis, porro. Dignissimos ducimus ratione totam fugit officiis blanditiis exercitationem, nisi vero architecto quibusdam impedit, earum '
  }
]

export default {
  head() {
    return {
      title: 'Recipes list'
    }
  },
  components: {
    RecipeCard
  },
  data() {
    return {
      recipes: []
    }
  },
  asyncData(context) {
    const data = sampleData
    return {
      recipes: data
    }
  },
  methods: {
    deleteRecipe(RecipeId) {
      // eslint-disable-next-line no-console
      console.log(`deleted ${RecipeId}`)
    }
  }
}
</script>
<style scoped></style>
