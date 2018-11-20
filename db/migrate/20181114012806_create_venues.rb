class CreateVenues < ActiveRecord::Migration[5.2]
  def change
    create_table :venues do |t|
      t.string :venue_id
      t.string :venue_name
      t.string :venue_alias
      t.float :latitude
      t.float :longitude
      t.string :address1
      t.string :address2
      t.string :address3
      t.string :city
      t.string :state
      t.string :zip_code
      t.timestamps
    end
  end
end
