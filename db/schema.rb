# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# Note that this schema.rb definition is the authoritative source for your
# database schema. If you need to create the application database on another
# system, you should be using db:schema:load, not running all the migrations
# from scratch. The latter is a flawed and unsustainable approach (the more migrations
# you'll amass, the slower it'll run and the greater likelihood for issues).
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema.define(version: 2018_11_14_012806) do

  # These are extensions that must be enabled in order to support this database
  enable_extension "plpgsql"

  create_table "events", force: :cascade do |t|
    t.string "name"
    t.integer "lat"
    t.integer "lng"
    t.integer "rating"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "pevents", force: :cascade do |t|
    t.string "venue_id"
    t.string "event_name"
    t.string "event_alias"
    t.string "event_id"
    t.integer "mon_start"
    t.integer "mon_end"
    t.integer "tues_start"
    t.integer "tues_end"
    t.integer "wed_start"
    t.integer "wed_end"
    t.integer "thurs_start"
    t.integer "thurs_end"
    t.integer "fri_start"
    t.integer "fri_end"
    t.integer "sat_start"
    t.integer "sat_end"
    t.integer "sun_start"
    t.integer "sun_end"
    t.string "tags", array: true
    t.integer "price"
  end

  create_table "tevents", force: :cascade do |t|
    t.string "venue_id"
    t.string "event_name"
    t.string "event_id"
    t.integer "start"
    t.integer "end"
    t.string "date"
    t.string "tags", array: true
    t.integer "price"
  end

  create_table "venues", force: :cascade do |t|
    t.string "venue_id"
    t.string "venue_name"
    t.string "venue_alias"
    t.float "latitude"
    t.float "longitude"
    t.string "address1"
    t.string "address2"
    t.string "address3"
    t.string "city"
    t.string "state"
    t.string "zip_code"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

end
