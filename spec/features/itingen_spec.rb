require 'rails_helper'

describe 'content' do
  before do
    visit root_path
  end

  describe 'homepage' do
    it 'should be reached successfully' do
      expect(page.status_code).to eq(200)
    end

    describe 'maps' do
      it 'should display google maps' do
        page.should have_css('div', :id => 'map')
      end

      it 'should display a location' do
        page.should have_css('h5', :class => 'card-title')
      end
    end

    describe 'sidebar' do
      describe 'menu' do
        it 'should have a menu' do
          page.should have_css('div', :id => 'mySidebar')
        end

        it 'should have an option to login' do
          page.should have_css('button', :text => 'Login')
        end

        it 'should have an option to sign up' do
          page.should have_css('button', :text => 'Register')
        end
      end
      it 'should have an itinerary' do
        page.should have_css('div', :class => 'card-header')
      end

      it 'should have a like button' do
        page.should have_css('a', :id => 'like')
      end

      it 'should have a dislike button' do
        page.should have_css('a', :id => 'dislike')
      end

      it 'should have a save current itinerary button' do
        page.should have_css('a', :id => 'like')
      end

      it 'should have a link to saved itineraries' do
        page.should have_css('button', :text => 'Liked Itineraries')
      end
    end

    describe 'liked itineraries' do
      it 'should have itineraries' do
        page.should have_css('div', :id => 'liked-itinerary-1')
        page.should have_css('div', :id => 'liked-itinerary-2')
      end

      it 'should have un-like button' do
        page.should have_css('button', :id => 'unlike')
      end

      it 'should have highlight button' do
        page.should have_css('button', :id => 'highlight-itin')
      end
    end 

    describe 'settings' do
      it 'should have time setting' do
        page.should have_css('div', :id => 'time-setting')
      end
      it 'should have radius setting' do
        page.should have_css('div', :id => 'radius-setting')
      end
      it 'should have radius helper indication' do
        page.should have_css('div', :id => 'radius-help')
      end
      it 'should have radius help window' do
        page.should have_css('div', :id => 'radius-help-window')
      end
      it 'should have money setting' do
        page.should have_css('div', :id => 'money-setting')
      end
      it 'should have start location setting' do
        page.should have_css('div', :id => 'locaiton-setting')
      end
      it 'should have location setting helper indication' do
        page.should have_css('div', :id => 'location-helper')
      end
      it 'should have location setting help window' do
        page.should have_css('div', :id => 'location-help-window')
      end
    end


  end
end
