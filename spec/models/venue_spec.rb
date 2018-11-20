RSpec.describe Event, type: :model do
  describe 'default event details' do
    let(:event) { create :event }

    it 'should initialize event with name and age' do
      expect(event.venue_name).to eq("Best Event Ever")
      expect(event.state).to eq('IL')
    end
  end

  describe 'default event details' do
    before do
      create :event
    end

    it 'should initialize event with name and age' do
      expect(Event.count).to eq 1

      w = Event.last

      expect(w.venue_name).to eq("Best Event Ever")
      expect(w.city).to eq("Chicago")
    end
  end
end

