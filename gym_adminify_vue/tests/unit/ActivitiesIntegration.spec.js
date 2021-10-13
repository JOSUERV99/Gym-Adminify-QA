import { shallowMount, createLocalVue } from '@vue/test-utils'
import Activities from '../../src/views/Activities.vue'
import Vuex from 'vuex';
jest.mock('axios');

const store = new Vuex.Store({
    state: {
        permissions: []
    },
    mutations: {
        setIsLoading(state,status) {
            state.isLoading = status
        }
    },
});

describe('Activities.vue integration test', () => {
  it('save modify activity using PUT request', async () => {

    // define actitivies component state using stub
    const activitiesViewStub = {
        activityStartTime_new: '10:30',
        activityEndTime_new: '10:30',
        activityDay_edit : 1,
        activities: [], 
    }

    // mount the actities component into a variable
    const wrapper = shallowMount(Activities, {
        data() {
          return activitiesViewStub
        },
        global: {
        mocks: {
          $store: store,
        }
    }});

    // create an spy to know if the put method have been called
    const spyPut = jest.spyOn(wrapper.vm, 'saveModifyActivity');
    
    // let's try to save the modified activity
    try {
      const activitiesDummy = [];
      await wrapper.vm.saveModifyActivity(activitiesDummy);
    }
    catch(err) {
      // expecting no error using the function
      expect(err).toBe(null);
    }

    // self plained
    expect(spyPut).toHaveBeenCalled();
  });
})