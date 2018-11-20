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
  end
end
