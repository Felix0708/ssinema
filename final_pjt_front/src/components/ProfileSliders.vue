<template>
  <div @mouseover = "btnOn" @mouseleave = "btnOff">
    <swiper :options = "swiperOptions" ref = "slider" >
      <MoviesCard
        v-for="(movie, idx) in movies"
        :key="idx"
        :movie="movie"
        class="col-lg-2 col-md-4 col-sm-6 col-xs-12"
      />
      <div class="swiper-pagination" slot="pagination"></div>
      <div 
        v-if="buttonOn"
        class="swiper-button-prev swiper-button-white" 
        slot="button-prev" 
        @click = "prev">    
      </div>
      <div 
      v-if="buttonOn"
      class="swiper-button-next swiper-button-white" 
      slot="button-next" 
      @click = "next"
      >
    </div>
    </swiper>
    <br>
  </div>
</template>

<script>
import MoviesCard from '../components/MoviesCard.vue'

export default {
  props:{
    movies:Array,
  },
  components:{
    MoviesCard,
  },
  data() {
    return {
      buttonOn : true,
      swiperOptions: {
          slidesPerView: 5,
          spaceBetween: 100,
          // loop: true,
          navigation: {
            nextEl: '#button-next-relacionados',
            prevEl: '#button-prev-relacionados'
          },
        }
    }
  },
  methods: {
    btnOn(){
      this.buttonOn = true
    },
    btnOff(){
      this.buttonOn = false
    },
    prev(){
      for (let i = 0; i < 5; i++){
        this.$refs.slider.$swiper.slidePrev()
      }
      this.$refs.slider.$swiper.slidePrev()
    },
    next(){
      for (let i = 0; i < 5; i++){
        this.$refs.slider.$swiper.slideNext()
      }
      this.$refs.slider.$swiper.slideNext()
    },
  }
}
</script>

<style>

</style>