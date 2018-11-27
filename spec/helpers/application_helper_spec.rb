require 'spec_helper'
require 'date'

describe ApplicationHelper do
	describe 'date_to_week_day' do

		it 'should return nil given invalid input' do
			expect(helper.date_to_week_day(nil)).to eq(nil)
			expect(helper.date_to_week_day(1)).to eq(nil)
			expect(helper.date_to_week_day('11/20/2018')).to eq(nil)
			expect(helper.date_to_week_day('11-20-2018')).to eq(nil)
		end

		it 'should convert a valid DateTime object to a week day string' do
			expect(helper.date_to_week_day(DateTime.new(2018, 11, 20))).to eq('tues')
			expect(helper.date_to_week_day(DateTime.new(2018, 11, 19))).to eq('mon')
			expect(helper.date_to_week_day(DateTime.new(2018, 11, 21))).to eq('weds')
			expect(helper.date_to_week_day(DateTime.new(2018, 11, 22))).to eq('thurs')
			expect(helper.date_to_week_day(DateTime.new(2018, 11, 23))).to eq('fri')
			expect(helper.date_to_week_day(DateTime.new(2018, 11, 24))).to eq('sat')
			expect(helper.date_to_week_day(DateTime.new(2018, 11, 25))).to eq('sun')
			expect(helper.date_to_week_day(DateTime.new(2007, 2, 14))).to eq('tues')
			expect(helper.date_to_week_day(DateTime.new(2019, 3, 2))).to eq('sat')
		end		
	end

	describe 'minutes_to_time_string' do

		it 'should return nil given invalid input' do
			expect(helper.minutes_to_time_string(-1)).to eq(nil)
			expect(helper.minutes_to_time_string(1440)).to eq(nil)
			expect(helper.minutes_to_time_string(1500)).to eq(nil)
		end

		it 'should convert minutes from midnight to a time string' do
			expect(helper.minutes_to_time_string(0)).to eq('12:00 AM')		
			expect(helper.minutes_to_time_string(1)).to eq('12:01 AM')		
			expect(helper.minutes_to_time_string(1439)).to eq('11:59 PM')		
			expect(helper.minutes_to_time_string(65)).to eq('1:05 AM')		
			expect(helper.minutes_to_time_string(630)).to eq('10:30 AM')
			expect(helper.minutes_to_time_string(0.4)).to eq('12:00 AM')		
			expect(helper.minutes_to_time_string(0.5)).to eq('12:01 AM')
			expect(helper.minutes_to_time_string(0.6)).to eq('12:01 AM')		
			expect(helper.minutes_to_time_string(912)).to eq('3:12 PM')
		end
	end

end