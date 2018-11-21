require 'spec_helper'
describe ApplicationHelper do
	it 'should return true' do
		assert helper.minutes_to_time(nil)
	end
end