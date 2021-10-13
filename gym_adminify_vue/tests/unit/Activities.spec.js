import { shallowMount, createLocalVue } from '@vue/test-utils'
import Activities from '../../src/views/Activities.vue'
import Vuex from 'vuex'

const store = new Vuex.Store({
                              state: {
                                permissions: []
                              },
                              mutations: {
                                setIsLoading(state,status){
                                  state.isLoading = status
                                }
                              },
                            })


describe('Activities.vue', () => {
  it('renders a message and responds correctly to user input', () => {
    const wrapper = shallowMount(Activities, {
      data() {
        return {
          activityStartTime_new: '10:30',
          activityEndTime_new: '10:30'
        }
      },
      global: {
      mocks: {
        $store: store,
      }
    } })

    expect(wrapper.vm.validateHours()).toBe(true)
  })
})