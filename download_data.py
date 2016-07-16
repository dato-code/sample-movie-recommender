#!/usr/bin/env python

#
# Downloads datasets for sample projects.
#

from os import path
import urllib
import zipfile

def download(url, target_file):
	"""Download a file from the url to the given target filename."""

	def report(blocks, block_size, total_size):
		percent = (100 * blocks * block_size) / total_size
		last_percent = (100 * (blocks - 1) * block_size) / total_size

		if percent > last_percent:
			print "  {0:.0f}% complete".format(percent)

	print "Downloading %s to %s..." % (url, target_file)
	urllib.urlretrieve(url, target_file, report)
	print "Download complete."

def unzip(file, target_dir):
	"""Unzip a zip archive to the given target directory."""

	print "Extracting %s to %s..." % (file, target_dir)
	with zipfile.ZipFile(file, 'r') as zfile:
		zfile.extractall(target_dir)
	print "Files extracted."

if __name__ == '__main__':

	# Path to the dataset: ../../datasets
	data_dir = './dataset'

	# MovieLens dataset collected by the GroupLens Research Project at the University of Minnesota.
	download("http://files.grouplens.org/datasets/movielens/ml-20m.zip", path.join(data_dir, 'ml-20m.zip'))
	unzip(path.join(data_dir, 'ml-20m.zip'), data_dir)
	download("https://static.turi.com/datasets/sample-movie-recommender/user_names.csv", path.join(data_dir, 'ml-20m/user_names.csv'))
	download("https://static.turi.com/datasets/sample-movie-recommender/movie_urls.csv", path.join(data_dir, 'ml-20m/movie_urls.csv'))
