import { shallowMount, createLocalVue } from '@vue/test-utils'
import Activities from '../../src/views/Activities.vue'
import Vuex from 'vuex'

const store = new Vuex.Store({
  state: {
    permissions: []
  },
  mutations: {
    setIsLoading(state, status) {
      state.isLoading = status
    }
  },
})

// * Test Suite for Activities.vue -> validateHours()
describe('Activities.vue -> validateHours() tests: ', () => {

  // Object that contains component
  let wrapper = null

  // Executes before test suite
  beforeAll(() => {
    // Component with default values
    wrapper = shallowMount(Activities, {
      data() {
        return {
          activityStartTime_new: '',
          activityEndTime_new: ''
        }
      },
      global: {
        mocks: {
          $store: store,
        }
      }
    })
  })

  // Executes after test suite
  afterAll(() => {
    wrapper.destroy()
  })

  // Case 1: Inputted start-time is after inputted end-time
  it('Start-time after end-time', () => {
    wrapper.setData({
      activityStartTime_new: '11:30',
      activityEndTime_new: '10:30'
    })

    expect(wrapper.vm.validateHours()).toBe(false)
  })

  // Case 2: Inputted start-time and end-time have the same time value
  it('Same start-time and end-time', () => {
    wrapper.setData({
      activityStartTime_new: '10:30',
      activityEndTime_new: '10:30'
    })

    expect(wrapper.vm.validateHours()).toBe(false)
  })

  // Case 3: Inputted start-time is before inputted end-time
  it('Start-time before end-time', () => {
    wrapper.setData({
      activityStartTime_new: '10:30',
      activityEndTime_new: '11:30'
    })

    expect(wrapper.vm.validateHours()).toBe(true)
  })

  // Case 4: Inputted start-time and end-time are both NULL values
  it('Null start-time and end-time', () => {
    wrapper.setData({
      activityStartTime_new: null,
      activityEndTime_new: null
    })

    expect(wrapper.vm.validateHours()).toBe(false)
  })

  // Case 5: Inputted start-time and end-time are both empty strings
  it('Empty start-time and end-time', () => {
    wrapper.setData({
      activityStartTime_new: '',
      activityEndTime_new: ''
    })

    expect(wrapper.vm.validateHours()).toBe(false)
  })

  // Case 6: Inputted start-time and end-time are both out of range
  it('Start-time and end-time out of range', () => {
    wrapper.setData({
      activityStartTime_new: '10:65',
      activityEndTime_new: '25:65'
    })
    
    expect(wrapper.vm.validateHours()).toBe(false)
  })

})